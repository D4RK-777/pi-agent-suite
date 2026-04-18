/**
 * Session Continuity Extension
 *
 * Lightweight session tracking: saves session state (task, events, duration)
 * as JSON under ~/.pi/sessions/ so the next session can load context about
 * what happened last time.
 *
 * This is the ONLY thing this extension does. Everything else that was in the
 * old hook-connector (Python hook calls, quality gates, MemPalace enforcement)
 * is handled by dedicated extensions:
 *   - prompt-context-injector.ts → MemPalace auto-injection
 *   - stop-hook-filer.ts → filing decisions to MemPalace
 *   - session-logger.ts → detailed JSONL event logging
 *   - security-gate.ts → blocking dangerous operations
 *   - auto-memory.ts → cross-session memory
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { existsSync, readFileSync, writeFileSync, mkdirSync, readdirSync, statSync } from "fs";
import { join } from "path";

const PI_ROOT = join(process.env.USERPROFILE || process.env.HOME || "", ".pi");
const SESSIONS_DIR = join(PI_ROOT, "sessions");

function ensureDir(path: string) {
  try { mkdirSync(path, { recursive: true }); } catch {}
}

interface SessionState {
  id: string;
  startTime: number;
  task: string;
  toolCalls: number;
  events: Array<{ type: string; ts: number; detail?: string }>;
}

let current: SessionState | null = null;

function sessionId(): string {
  return `session-${new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19)}`;
}

function save(state: SessionState) {
  try {
    ensureDir(SESSIONS_DIR);
    writeFileSync(join(SESSIONS_DIR, `${state.id}.json`), JSON.stringify(state, null, 2), "utf8");
  } catch (err) {
    process.stderr.write(`[hook-connector] save failed: ${err}\n`);
  }
}

function loadMostRecent(): SessionState | null {
  try {
    const files = readdirSync(SESSIONS_DIR)
      .filter(f => f.endsWith(".json") && f.startsWith("session-"))
      .map(f => ({ name: f, mtime: statSync(join(SESSIONS_DIR, f)).mtime.getTime() }))
      .sort((a, b) => b.mtime - a.mtime);
    if (files.length === 0) return null;
    return JSON.parse(readFileSync(join(SESSIONS_DIR, files[0].name), "utf8"));
  } catch (err) {
    process.stderr.write(`[hook-connector] loadMostRecent failed: ${err}\n`);
    return null;
  }
}

export default function (pi: ExtensionAPI) {
  pi.on("session_start", async (_e, ctx) => {
    current = { id: sessionId(), startTime: Date.now(), task: "", toolCalls: 0, events: [] };

    // Load previous session summary for continuity
    const prev = loadMostRecent();
    if (prev && prev.id !== current.id) {
      const mins = Math.round((Date.now() - prev.startTime) / 60000);
      const summary = prev.task ? `Last session (${mins}m ago): "${prev.task}" — ${prev.toolCalls} tool calls` : "";
      if (summary) {
        ctx.ui.notify(summary, "info");
      }
    }
  });

  pi.on("agent_start", () => {
    if (current) current.events.push({ type: "agent_start", ts: Date.now() });
  });

  pi.on("tool_execution_end", (e: any) => {
    if (current) {
      current.toolCalls++;
      current.events.push({ type: "tool", ts: Date.now(), detail: e?.toolName || e?.tool || "?" });
    }
  });

  pi.on("agent_end", () => {
    if (current) {
      current.events.push({ type: "agent_end", ts: Date.now() });
      save(current);
    }
  });

  pi.on("session_shutdown", () => {
    if (current) {
      current.events.push({ type: "shutdown", ts: Date.now() });
      save(current);
      current = null;
    }
  });
}
