/**
 * JSONL Session Logger Extension
 *
 * Writes structured per-event logs to ~/.pi/sessions/logs/YYYY-MM-DD.jsonl.
 * One JSONL line per tool call + one per assistant/user message end.
 *
 * Substrate for:
 *   - the Stop hook (so session-close can introspect what actually happened)
 *   - Auto-Dream nightly consolidation (pattern mining over rolling logs)
 *   - ad-hoc analytics ("how many times did I hit mempalace_search this week?")
 *
 * Design notes:
 *   - Fire-and-forget writes; never block the agent loop.
 *   - Never log secrets. We truncate Bash input / Read paths and redact env-looking args.
 *   - Each line is self-contained JSON — no cross-line state.
 *   - Uses ctx.sessionManager.getSessionId() for correlation across events.
 */

import type { ExtensionAPI, ToolExecutionStartEvent, ToolExecutionEndEvent, MessageEndEvent } from "@mariozechner/pi-coding-agent";
import { appendFile, mkdir } from "fs/promises";
import { homedir } from "os";
import { join } from "path";

const LOG_DIR = join(homedir(), ".pi", "sessions", "logs");

// Track start timestamps so tool_execution_end can compute duration.
// Capped + TTL-swept so a killed-mid-flight tool can't leak memory across a long session.
const MAX_INFLIGHT = 512;
const INFLIGHT_TTL_MS = 10 * 60 * 1000;
const startTimes = new Map<string, number>();
function sweepInflight(now: number) {
  if (startTimes.size < MAX_INFLIGHT) return;
  for (const [id, started] of startTimes) {
    if (now - started > INFLIGHT_TTL_MS) startTimes.delete(id);
  }
}

function todayFile(): string {
  const d = new Date();
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return join(LOG_DIR, `${y}-${m}-${day}.jsonl`);
}

/** Keep logs small; redact anything that sniffs like a secret. */
function excerpt(value: unknown, max = 400): string {
  if (value === undefined || value === null) return "";
  const s = typeof value === "string" ? value : JSON.stringify(value);
  // Redact by key name (api_key=..., token: "..."), then by known token prefixes.
  const redacted = s
    .replace(/(api[_-]?key|access[_-]?token|refresh[_-]?token|secret|password|bearer|authorization)["':=\s]+[^"'\s,}]+/gi, "$1=<redacted>")
    .replace(/sk-[A-Za-z0-9_\-]{20,}/g, "sk-<redacted>")                    // OpenAI / Anthropic / MiniMax
    .replace(/ghp_[A-Za-z0-9]{20,}/g, "ghp_<redacted>")                      // GitHub PAT
    .replace(/github_pat_[A-Za-z0-9_]{20,}/g, "github_pat_<redacted>")       // GitHub fine-grained PAT
    .replace(/gho_[A-Za-z0-9]{20,}/g, "gho_<redacted>")                      // GitHub OAuth
    .replace(/xox[abprs]-[A-Za-z0-9-]{10,}/g, "xox*-<redacted>")             // Slack tokens
    .replace(/AKIA[0-9A-Z]{16}/g, "AKIA<redacted>")                          // AWS access key ID
    .replace(/(aws_secret_access_key["':=\s]+)[A-Za-z0-9/+=]{20,}/gi, "$1<redacted>")
    .replace(/eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}/g, "<jwt-redacted>")
    .replace(/-----BEGIN[^-]+PRIVATE KEY-----[\s\S]*?-----END[^-]+PRIVATE KEY-----/g, "<private-key-redacted>");
  return redacted.length > max ? redacted.slice(0, max) + "…" : redacted;
}

/** Strip extension-injected prologue blocks so logs reflect what the USER actually said. */
function stripInjectionTags(text: string): string {
  // Tags we know we inject in front of user prompts.
  const tags = ["mempalace-context", "project-instructions", "session-git-context", "pi-memory", "pi-tasks"];
  let out = text;
  for (const tag of tags) {
    const rx = new RegExp(`<${tag}>[\\s\\S]*?</${tag}>\\s*`, "g");
    out = out.replace(rx, "");
  }
  return out.trim();
}

function extractMessageText(message: any): { role: string; text: string; contentTypes: string[] } {
  const role = message?.role || "unknown";
  const content = message?.content;
  if (typeof content === "string") {
    return { role, text: role === "user" ? stripInjectionTags(content) : content, contentTypes: ["text"] };
  }
  if (!Array.isArray(content)) {
    return { role, text: "", contentTypes: [] };
  }
  const parts: string[] = [];
  const types: string[] = [];
  for (const block of content) {
    if (!block || typeof block !== "object") continue;
    const t = block.type || "unknown";
    types.push(t);
    if (t === "text" && typeof block.text === "string") {
      parts.push(block.text);
    } else if (t === "toolCall" && block.name) {
      parts.push(`[tool:${block.name}]`);
    } else if (t === "thinking" && typeof block.thinking === "string") {
      // Note thinking length but don't log the content — keeps logs lean.
      parts.push(`[thinking:${block.thinking.length}chars]`);
    }
  }
  const joined = parts.join(" ");
  return { role, text: role === "user" ? stripInjectionTags(joined) : joined, contentTypes: types };
}

// Logging failures used to be completely silent (bare `catch {}`). That means
// a full disk or permissions regression would cause invisible data loss — the
// user would only discover it by explicitly checking logs days later. We now
// surface the first failure to stderr + optionally to the UI once per session.
let writeFailureCount = 0;
let notifyFailureOnce: ((msg: string) => void) | null = null;

async function writeLine(obj: Record<string, unknown>): Promise<void> {
  try {
    await mkdir(LOG_DIR, { recursive: true });
    await appendFile(todayFile(), JSON.stringify(obj) + "\n", "utf8");
  } catch (err) {
    writeFailureCount++;
    // Never let logging interfere with the agent loop — but also never swallow silently.
    if (writeFailureCount === 1) {
      const msg = `[session-logger] write failed: ${err instanceof Error ? err.message : String(err)}`;
      try { process.stderr.write(msg + "\n"); } catch {}
      try { notifyFailureOnce?.("Session logger is failing to write — logs may be incomplete. See stderr."); } catch {}
    }
    // Subsequent failures: stderr only, rate-limited every 100 to avoid spam on sustained failure.
    else if (writeFailureCount % 100 === 0) {
      try { process.stderr.write(`[session-logger] ${writeFailureCount} writes failed (suppressing further warnings)\n`); } catch {}
    }
  }
}

export default function (pi: ExtensionAPI) {
  pi.on("tool_execution_start", (event: ToolExecutionStartEvent) => {
    const now = Date.now();
    sweepInflight(now);
    startTimes.set(event.toolCallId, now);
  });

  pi.on("tool_execution_end", async (event: ToolExecutionEndEvent, ctx) => {
    const started = startTimes.get(event.toolCallId);
    const now = Date.now();
    const durationMs = started ? now - started : undefined;
    startTimes.delete(event.toolCallId);

    const resultText = Array.isArray(event.result?.content)
      ? event.result.content
          .filter((c: any) => c?.type === "text")
          .map((c: any) => c.text)
          .join("\n")
      : "";

    await writeLine({
      ts: new Date(now).toISOString(),
      session_id: ctx.sessionManager.getSessionId(),
      type: "tool",
      tool: event.toolName,
      tool_call_id: event.toolCallId,
      is_error: event.isError,
      duration_ms: durationMs,
      result_excerpt: excerpt(resultText, 300),
    });
  });

  pi.on("message_end", async (event: MessageEndEvent, ctx) => {
    const { role, text, contentTypes } = extractMessageText(event.message);
    // Skip toolResult messages — covered by tool_execution_end already.
    if (role === "toolResult") return;
    await writeLine({
      ts: new Date().toISOString(),
      session_id: ctx.sessionManager.getSessionId(),
      type: "message",
      role,
      content_types: contentTypes,
      text_excerpt: excerpt(text, 500),
    });
  });

  pi.on("session_start", async (_event, ctx) => {
    // Reset per-session failure counter + wire up the one-time UI notifier.
    writeFailureCount = 0;
    notifyFailureOnce = (msg: string) => {
      try { ctx.ui.notify(msg, "warning"); } catch {}
    };
    await writeLine({
      ts: new Date().toISOString(),
      session_id: ctx.sessionManager.getSessionId(),
      type: "session_start",
      reason: (_event as any).reason,
      cwd: ctx.cwd,
    });
    ctx.ui.notify("Session logger armed (JSONL at ~/.pi/sessions/logs/)", "info");
  });

  pi.on("session_shutdown", async (_event, ctx) => {
    await writeLine({
      ts: new Date().toISOString(),
      session_id: ctx.sessionManager.getSessionId(),
      type: "session_shutdown",
    });
  });
}
