/**
 * MemPalace Tools Extension for PI Agent
 *
 * Gives the MiniMax (or any pi) agent live access to MemPalace:
 *   - mempalace_search:      hybrid BM25+vector recall over ~3K+ drawers
 *   - mempalace_list_wings:  enumerate wings so the agent picks the right one
 *   - mempalace_add_drawer:  file verbatim content into a wing/room
 *   - mempalace_stats:       palace health (drawer count, avg query ms)
 *
 * All ops shell to Python — MemPalace is python-native (ChromaDB backend).
 * The `mempalace_fast` wrapper at ~/.pi/agent/bin handles sys.path + palace resolution.
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";
import { spawn } from "child_process";
import { join } from "path";

const PI_ROOT = join(process.env.USERPROFILE || process.env.HOME || "", ".pi");
const BIN_DIR = join(PI_ROOT, "agent", "bin");

function runPython(code: string, stdin?: string, timeoutMs = 15000): Promise<{ stdout: string; stderr: string; code: number }> {
  return new Promise((resolve) => {
    const python = process.platform === "win32" ? "python" : "python3";
    const proc = spawn(python, ["-X", "utf8", "-c", code], {
      env: { ...process.env, PYTHONIOENCODING: "utf8" },
      shell: false,
    });
    let stdout = "";
    let stderr = "";
    proc.stdout.on("data", (d) => (stdout += d.toString()));
    proc.stderr.on("data", (d) => (stderr += d.toString()));
    proc.on("close", (code) => resolve({ stdout, stderr, code: code || 0 }));
    proc.on("error", (err) => {
      stderr += err.message;
      resolve({ stdout, stderr, code: 1 });
    });
    if (stdin) {
      proc.stdin.write(stdin);
      proc.stdin.end();
    }
    setTimeout(() => {
      proc.kill();
      resolve({ stdout, stderr: stderr + "\n[timeout]", code: 124 });
    }, timeoutMs);
  });
}

export default function (pi: ExtensionAPI) {
  // ═══════════════════════════════════════════════════════════════════
  // SEARCH
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "mempalace_search",
    label: "MemPalace Search",
    description:
      "Semantic + BM25 recall over the palace. Use BEFORE writing code — the palace stores verbatim past decisions, patterns, and code. " +
      "Narrow with `wing` when you know the domain (e.g. 'konekt_nextjs' for the Gloss Next.js app, 'expert-knowledge' for curated vault notes).",
    parameters: Type.Object({
      query: Type.String({ description: "Natural language query. Be specific — 'jwt refresh token flow' beats 'auth'." }),
      wing: Type.Optional(
        Type.String({
          description: "Limit to one wing. Common: konekt_nextjs (Gloss product code), expert-knowledge (vault notes), mempalace (general).",
        }),
      ),
      n: Type.Optional(Type.Number({ description: "Max results (default 5)", default: 5 })),
    }),
    async execute(_toolCallId, params) {
      // Fast path: daemon at 127.0.0.1:8787.
      try {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), 1200);
        const res = await fetch("http://127.0.0.1:8787/search", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ q: params.query, wing: params.wing, n: params.n || 5 }),
          signal: controller.signal,
        });
        clearTimeout(timer);
        if (res.ok) {
          const hits = await res.json();
          return { content: [{ type: "text", text: JSON.stringify(hits, null, 2) }] };
        }
      } catch {
        // daemon unreachable — fall through to spawn
      }

      const code = `
import sys, json
sys.path.insert(0, r'${BIN_DIR.replace(/\\/g, "\\\\")}')
from mempalace_fast import search
wing = ${params.wing ? JSON.stringify(params.wing) : "None"}
n = ${params.n || 5}
out = search(${JSON.stringify(params.query)}, wing=wing, n=n)
results = out.get("results", [])
print(json.dumps([
    {
        "similarity": round(r.get("similarity", 0), 3),
        "wing": r.get("wing", ""),
        "room": r.get("room", ""),
        "source": (r.get("source_file", "") or "").split("\\\\")[-1][:80],
        "text": (r.get("text", "") or "")[:600],
    }
    for r in results
], indent=2))
`;
      const res = await runPython(code);
      if (res.code !== 0) {
        return { content: [{ type: "text", text: `MemPalace error:\n${res.stderr}` }] };
      }
      const hits = res.stdout.trim();
      return {
        content: [{ type: "text", text: hits || "No results." }],
      };
    },
  });

  // ═══════════════════════════════════════════════════════════════════
  // LIST WINGS
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "mempalace_list_wings",
    label: "MemPalace List Wings",
    description: "Enumerate all wings and drawer counts so you can pick the right wing for a search.",
    parameters: Type.Object({}),
    async execute() {
      const code = `
import sys, json
sys.path.insert(0, r'${BIN_DIR.replace(/\\/g, "\\\\")}')
from mempalace_fast import PALACE
from mempalace.backends.chroma import ChromaBackend
backend = ChromaBackend()
col = backend.get_collection(PALACE, "mempalace_drawers", create=False)
got = col.get(include=["metadatas"])
metas = got.get("metadatas") or []
wings: dict[str, int] = {}
for m in metas:
    if not m:
        continue
    w = m.get("wing") or "(none)"
    wings[w] = wings.get(w, 0) + 1
print(json.dumps(sorted(wings.items(), key=lambda kv: -kv[1])))
`;
      const res = await runPython(code);
      if (res.code !== 0) {
        return { content: [{ type: "text", text: `MemPalace error:\n${res.stderr}` }] };
      }
      return { content: [{ type: "text", text: res.stdout.trim() }] };
    },
  });

  // ═══════════════════════════════════════════════════════════════════
  // ADD DRAWER (verbatim filing)
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "mempalace_add_drawer",
    label: "MemPalace Add Drawer",
    description:
      "File verbatim content into a MemPalace wing. Use for the user's exact words, decisions, or code they wrote. " +
      "Do NOT paraphrase — verbatim is the whole point. Skip filing your own generated prose (the Stop hook handles session summaries).",
    parameters: Type.Object({
      content: Type.String({ description: "Verbatim text to file. Can be multi-line." }),
      wing: Type.String({
        description: "Target wing. Use konekt_nextjs for Gloss product context, expert-knowledge for vault-grade patterns, mempalace for general notes.",
      }),
      source: Type.Optional(Type.String({ description: "Optional source label (e.g. 'chat-2026-04-16')" })),
    }),
    async execute(_toolCallId, params) {
      const source = params.source || `pi-session-${Date.now()}`;

      // Fast path: daemon at 127.0.0.1:8787/add. Same 15,000-drawer palace stays
      // warm in memory — no Python cold-start per call.
      try {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), 2500);
        const res = await fetch("http://127.0.0.1:8787/add", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            content: params.content,
            wing: params.wing,
            room: "notes",
            source,
            agent: "pi-minimax",
          }),
          signal: controller.signal,
        });
        clearTimeout(timer);
        if (res.ok) {
          const data = await res.json();
          return { content: [{ type: "text", text: JSON.stringify(data) }] };
        }
      } catch {
        // daemon unreachable — fall through to spawn
      }

      // Fallback: spawn Python (cold ~2s). Only hit if daemon is down.
      const code = `
import sys, json
sys.path.insert(0, r'${BIN_DIR.replace(/\\/g, "\\\\")}')
from mempalace_fast import PALACE
from mempalace.miner import get_collection, add_drawer
text = sys.stdin.read()
col = get_collection(PALACE, create=True)
add_drawer(
    collection=col,
    wing=${JSON.stringify(params.wing)},
    room="notes",
    content=text,
    source_file=${JSON.stringify(source)},
    chunk_index=0,
    agent="pi-minimax",
)
print(json.dumps({"filed": True, "wing": ${JSON.stringify(params.wing)}, "chars": len(text)}))
`;
      const res = await runPython(code, params.content);
      if (res.code !== 0) {
        return { content: [{ type: "text", text: `MemPalace add_drawer failed:\n${res.stderr}` }] };
      }
      return { content: [{ type: "text", text: res.stdout.trim() || "Filed." }] };
    },
  });

  // ═══════════════════════════════════════════════════════════════════
  // STATS
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "mempalace_stats",
    label: "MemPalace Stats",
    description: "Palace health: total drawer count, recent avg query latency. Use to confirm MemPalace is alive.",
    parameters: Type.Object({}),
    async execute() {
      const code = `
import sys, json
sys.path.insert(0, r'${BIN_DIR.replace(/\\/g, "\\\\")}')
from mempalace_fast import status
print(json.dumps(status(), indent=2))
`;
      const res = await runPython(code);
      if (res.code !== 0) {
        return { content: [{ type: "text", text: `MemPalace error:\n${res.stderr}` }] };
      }
      return { content: [{ type: "text", text: res.stdout.trim() }] };
    },
  });

  pi.on("session_start", async (_e, ctx) => {
    ctx.ui.notify("MemPalace tools loaded (search, list_wings, add_drawer, stats)", "info");
  });
}
