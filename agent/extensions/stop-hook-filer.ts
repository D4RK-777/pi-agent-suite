/**
 * Stop Hook — Auto-File Session Decisions into MemPalace
 *
 * On each `agent_end`, scan newly seen user messages for verbatim quotes
 * worth filing. Route to a wing via keyword heuristics, then file via
 * mempalace.miner.add_drawer (Python spawn — latency-insensitive).
 *
 * Doctrine:
 *   - Verbatim only. NEVER paraphrase. The user's exact words or nothing.
 *   - Never file our own (assistant) output. The user's explicit decisions
 *     are the signal; our explanations are noise.
 *   - Filing must be idempotent — the same message seen twice is only filed once.
 *
 * Triggering heuristics (AND-composed with length > MIN_CHARS):
 *   - Decision verbs: let's, we're going, we decided, I want, stop doing, don't
 *   - Doctrine markers: "never", "always", "the rule is", "prefer"
 *   - Contains a URL, code block, or file path (tends to be substantive)
 *
 * Short acknowledgements, thanks, and "yeah cool" style messages are skipped —
 * they're session noise, not knowledge.
 */

import type { ExtensionAPI, AgentEndEvent } from "@mariozechner/pi-coding-agent";
import { spawn } from "child_process";
import { createHash } from "crypto";
import { appendFile, mkdir } from "fs/promises";
import { homedir } from "os";
import { join } from "path";

const PI_ROOT = join(process.env.USERPROFILE || process.env.HOME || "", ".pi");
const BIN_DIR = join(PI_ROOT, "agent", "bin");
const ERROR_LOG = join(homedir(), ".pi", "sessions", "stop-hook-errors.log");
const MIN_CHARS = 80;

async function logError(line: string): Promise<void> {
  try {
    await mkdir(join(homedir(), ".pi", "sessions"), { recursive: true });
    await appendFile(ERROR_LOG, `${new Date().toISOString()} ${line}\n`, "utf8");
  } catch {
    // best-effort; never throw from logging
  }
}

const DECISION_MARKERS = [
  /\blet['']?s\s+(use|go|try|build|avoid|not|stop)/i,
  /\bwe['']?(re|are|ve)\s+(going|doing|using|building|switching|moving)/i,
  /\bwe\s+(decided|chose|agreed|settled)/i,
  /\bi\s+(want|need|prefer|hate|love|always|never|don['']?t)/i,
  /\b(stop|don['']?t)\s+(doing|using|making|putting|writing|mocking|paraphrasing)/i,
  /\b(never|always)\s+(do|use|mock|paraphrase|commit|push|edit|write|read)/i,
  /\bthe\s+(rule|pattern|convention|doctrine)\s+is/i,
  /\bprefer\s+\w+\s+(over|to|instead)/i,
  /\breason\s+(we|I)['']?(re|ve|m)\s+(doing|using|building|switching)/i,
];

const CODE_OR_URL = /(```|https?:\/\/|[A-Z]:\\[^\s"]+|\/\w+\/[\w./-]+|\.tsx?\b|\.pyw?\b)/;

interface WingRoute {
  wing: string;
  room: string;
}

function routeWing(text: string): WingRoute {
  const t = text.toLowerCase();
  if (/\b(gloss|konekt|next\.?js|react|tsx?\b|tailwind|mui|phosphor|nextauth|radix)\b/.test(t)) {
    return { wing: "konekt_nextjs", room: "decisions" };
  }
  if (/\b(obsidian|vault|omegad4rkmynd|shadowvault|wiki|karpathy|frontmatter|dataview)\b/.test(t)) {
    return { wing: "expert-knowledge", room: "vault-ops" };
  }
  if (/\b(mempalace|chroma|embedding|hnsw|bm25|drawer|daemon|pi\s+agent|minimax)\b/.test(t)) {
    return { wing: "mempalace", room: "system-design" };
  }
  if (/\b(hook|skill|claude\s*code|agent|subagent|extension)\b/.test(t)) {
    return { wing: "expert-orchestration", room: "agentic-patterns" };
  }
  if (/\b(security|auth|jwt|session|token|xss|sql|csrf|wcag|a11y)\b/.test(t)) {
    return { wing: "expert-security", room: "guards" };
  }
  return { wing: "mempalace", room: "notes" };
}

function shouldFile(text: string): boolean {
  if (text.length < MIN_CHARS) return false;
  // Skip pure thanks / acknowledgement blobs even if long.
  if (/^(thanks?|thx|cheers|cool|nice|perfect|amazing|beautiful|love it|great)[\s\W]*$/i.test(text)) {
    return false;
  }
  const hitsDecision = DECISION_MARKERS.some((rx) => rx.test(text));
  if (hitsDecision) return true;
  // Long messages with code/URL/path are usually substantive specs.
  if (text.length > 300 && CODE_OR_URL.test(text)) return true;
  return false;
}

function stripInjectionTags(text: string): string {
  const tags = ["mempalace-context", "project-instructions", "session-git-context", "pi-memory", "pi-tasks"];
  let out = text;
  for (const tag of tags) {
    const rx = new RegExp(`<${tag}>[\\s\\S]*?</${tag}>\\s*`, "g");
    out = out.replace(rx, "");
  }
  return out.trim();
}

function extractUserText(message: any): string {
  if (!message || message.role !== "user") return "";
  const content = message.content;
  const raw =
    typeof content === "string"
      ? content
      : Array.isArray(content)
      ? content
          .filter((c: any) => c?.type === "text" && typeof c.text === "string")
          .map((c: any) => c.text)
          .join("\n")
      : "";
  return stripInjectionTags(raw);
}

function hashKey(wing: string, text: string): string {
  return createHash("sha1").update(wing + "::" + text).digest("hex").slice(0, 16);
}

const DAEMON_URL = process.env.PI_MEMPALACE_DAEMON_URL || "http://127.0.0.1:8787";

// Fast path: the warm daemon can file a drawer in ~200ms vs ~2s for Python spawn.
// Returns null if the daemon is unreachable so the caller falls back to spawn.
async function fileViaDaemon(
  wing: string,
  room: string,
  text: string,
  sessionId: string,
): Promise<{ ok: boolean } | null> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 3000);
  try {
    const res = await fetch(`${DAEMON_URL}/add`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        content: text,
        wing,
        room,
        source: `pi-session-${sessionId}`,
        agent: "pi-stop-hook",
      }),
      signal: controller.signal,
    });
    if (!res.ok) {
      const body = await res.text().catch(() => "");
      void logError(`daemon http=${res.status} wing=${wing} body=${body.slice(0, 300)}`);
      return { ok: false };
    }
    return { ok: true };
  } catch {
    // daemon unreachable → signal fallback
    return null;
  } finally {
    clearTimeout(timer);
  }
}

function fileViaSpawn(wing: string, room: string, text: string, sessionId: string): Promise<{ ok: boolean }> {
  return new Promise((resolve) => {
    const python = process.platform === "win32" ? "python" : "python3";
    const code = `
import sys, json
sys.path.insert(0, r'${BIN_DIR.replace(/\\/g, "\\\\")}')
from mempalace_fast import PALACE
from mempalace.miner import get_collection, add_drawer
text = sys.stdin.read()
col = get_collection(PALACE, create=True)
add_drawer(
    collection=col,
    wing=${JSON.stringify(wing)},
    room=${JSON.stringify(room)},
    content=text,
    source_file=${JSON.stringify("pi-session-" + sessionId)},
    chunk_index=0,
    agent="pi-stop-hook",
)
print("ok")
`;
    const proc = spawn(python, ["-X", "utf8", "-c", code], {
      env: { ...process.env, PYTHONIOENCODING: "utf8" },
      shell: false,
      windowsHide: true,
      stdio: ["pipe", "pipe", "pipe"],
    });
    let stderr = "";
    let stdout = "";
    let settled = false;
    const done = (ok: boolean, reason?: string) => {
      if (settled) return;
      settled = true;
      if (!ok) {
        void logError(`spawn wing=${wing} room=${room} reason=${reason || "unknown"} stderr=${stderr.slice(0, 500)}`);
      }
      resolve({ ok });
    };
    proc.stdout.on("data", (d) => (stdout += d.toString()));
    proc.stderr.on("data", (d) => (stderr += d.toString()));
    proc.on("close", (code) => done(code === 0 && stdout.includes("ok"), `exit=${code}`));
    proc.on("error", (err) => done(false, `spawn=${err.message}`));
    try {
      proc.stdin.write(text);
      proc.stdin.end();
    } catch (err) {
      done(false, `stdin=${(err as Error).message}`);
    }
    // Hard timeout — we never block the agent loop on filing.
    setTimeout(() => {
      try { proc.kill(); } catch {}
      done(false, "timeout");
    }, 8000);
  });
}

// Filing primitive: try the daemon first, fall back to Python spawn if it's down.
async function fileDrawer(wing: string, room: string, text: string, sessionId: string): Promise<{ ok: boolean }> {
  const viaDaemon = await fileViaDaemon(wing, room, text, sessionId);
  if (viaDaemon !== null) return viaDaemon;
  return fileViaSpawn(wing, room, text, sessionId);
}

export default function (pi: ExtensionAPI) {
  // Per-session dedupe cache. Reset on session_start.
  const filedHashes = new Set<string>();
  let lastProcessedTs = 0;
  let filedThisSession = 0;

  pi.on("session_start", () => {
    filedHashes.clear();
    lastProcessedTs = 0;
    filedThisSession = 0;
  });

  pi.on("agent_end", async (event: AgentEndEvent, ctx) => {
    const sessionId = ctx.sessionManager.getSessionId();
    let newestTs = lastProcessedTs;
    const toFile: Array<{ wing: string; room: string; text: string }> = [];

    for (const msg of event.messages) {
      const m = msg as any;
      if (m.role !== "user") continue;
      if (typeof m.timestamp !== "number" || m.timestamp <= lastProcessedTs) continue;
      newestTs = Math.max(newestTs, m.timestamp);
      const text = extractUserText(m);
      if (!shouldFile(text)) continue;
      const { wing, room } = routeWing(text);
      const h = hashKey(wing, text);
      if (filedHashes.has(h)) continue;
      filedHashes.add(h);
      toFile.push({ wing, room, text });
    }
    lastProcessedTs = newestTs;

    if (toFile.length === 0) return;

    // Fire all writes in parallel but don't block agent_end return too long.
    // (agent_end awaits its handlers but we keep file ops short with the timeout.)
    const results = await Promise.all(toFile.map((d) => fileDrawer(d.wing, d.room, d.text, sessionId)));
    const successes = results.filter((r) => r.ok).length;
    const failures = results.length - successes;
    filedThisSession += successes;
    if (ctx.hasUI) {
      const failNote = failures ? ` (${failures} failed — see ${ERROR_LOG})` : "";
      ctx.ui.notify(`Stop hook filed ${successes} drawer(s)${failNote} [session total: ${filedThisSession}]`, failures ? "warning" : "info");
    }
  });
}
