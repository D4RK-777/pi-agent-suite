/**
 * Prompt Context Injector for PI Agent
 *
 * Mirrors Claude Code's UserPromptSubmit hook behavior inside pi, but smarter:
 * on every prompt, fires PARALLEL MemPalace queries — one generic catch-all
 * plus one wing-filtered query per detected domain (frontend/react → konekt_nextjs,
 * mempalace/palace → mempalace wing, etc.). Deep domain knowledge surfaces
 * alongside serendipitous hits.
 *
 * Flow:
 *   user types prompt
 *     → input event fires
 *     → detectWings() scans keywords → picks relevant wings
 *     → Promise.all([generic top-3, per-wing top-5])   (all via daemon, parallel)
 *     → merge + dedupe by (source, first 120 chars of text)
 *     → prepend <mempalace-context> block with each group labeled
 *
 * Budgets:
 *   Daemon:        ≤ 500ms per query (all run in parallel — ceiling = slowest)
 *   Spawn fallback: ≤ 3500ms per query (only if daemon is dead)
 *   Hard ceiling:  fire-and-forget — if we overshoot, bail silently.
 *
 * Skip rules:
 *   - Extension-originated prompts (no injection loops)
 *   - < 12 chars (trivial prompts don't benefit from context)
 *   - Slash commands / session control
 *   - Prompts already containing <mempalace-context>
 */

import type { ExtensionAPI, InputEvent, InputEventResult } from "@mariozechner/pi-coding-agent";
import { spawn } from "child_process";
import { join } from "path";

const PI_ROOT = join(process.env.USERPROFILE || process.env.HOME || "", ".pi");
const BIN_DIR = join(PI_ROOT, "agent", "bin");

const DAEMON_URL = process.env.PI_MEMPALACE_DAEMON_URL || "http://127.0.0.1:8787";
const DAEMON_BUDGET_MS = 500;
const SPAWN_BUDGET_MS = 3500;
const MIN_PROMPT_CHARS = 12;
const GENERIC_N = 3;
const DOMAIN_N = 5;

interface Hit {
  similarity: number;
  wing: string;
  room: string;
  source: string;
  text: string;
}

// ── Domain → wing routing ────────────────────────────────────────────────────
// Keyword presence triggers a wing-scoped query in parallel with the generic one.
// The user's MemPalace is heavily weighted toward `konekt_nextjs` (12,548 drawers
// — the Gloss frontend/Next.js app), so most code keywords route there.
// Keep this list short and high-signal — every keyword fires an extra query.
const DOMAIN_WING_MAP: Array<{ wing: string; keywords: string[]; label: string }> = [
  {
    wing: "konekt_nextjs",
    label: "Gloss / Next.js / frontend code",
    keywords: [
      // product names
      "gloss", "konekt",
      // framework
      "next.js", "nextjs", "next ", "app router", "server component", "server action", "route handler",
      "api route",
      // react / ui
      "react", "component", "hook", "props", "state", "context", "useeffect", "usestate",
      "tsx", "jsx",
      // styling
      "tailwind", "styled", "css-in-js", "theme",
      // generic frontend / ui surface
      "frontend", " ui ", "page", "layout", "navbar", "sidebar", "modal", "dialog", "button",
      "form", "input field", "dropdown", "accessibility", "a11y", "wcag",
      // auth surface we've touched
      "auth", "login", "session", "jwt", "oauth",
    ],
  },
  {
    wing: "mempalace",
    label: "MemPalace / palace internals",
    keywords: [
      "mempalace", " palace", "drawer", "wing", "ingest", "mine", "miner",
      "chroma", "vector", "embedding", "bm25", "retrieval", "rag",
    ],
  },
  {
    wing: "expert-knowledge",
    label: "curated vault knowledge",
    keywords: [
      "pattern", "decision", "adr", "architecture", "best practice", "convention", "rule of thumb",
    ],
  },
];

function detectWings(prompt: string): Array<{ wing: string; label: string }> {
  const lower = prompt.toLowerCase();
  const out: Array<{ wing: string; label: string }> = [];
  for (const entry of DOMAIN_WING_MAP) {
    if (entry.keywords.some((kw) => lower.includes(kw))) {
      out.push({ wing: entry.wing, label: entry.label });
    }
  }
  return out;
}

// ── Daemon + spawn search primitives ─────────────────────────────────────────
async function searchViaDaemon(query: string, n: number, wing?: string): Promise<Hit[] | null> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), DAEMON_BUDGET_MS);
  try {
    const body: Record<string, unknown> = { q: query, n };
    if (wing) body.wing = wing;
    const res = await fetch(`${DAEMON_URL}/search`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      signal: controller.signal,
    });
    if (!res.ok) return null;
    const data = (await res.json()) as Hit[] | { error?: string };
    return Array.isArray(data) ? data : null;
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}

function searchViaSpawn(query: string, n: number, wing?: string): Promise<Hit[]> {
  return new Promise((resolve) => {
    const python = process.platform === "win32" ? "python" : "python3";
    const wingLiteral = wing ? JSON.stringify(wing) : "None";
    const code = `
import sys, json
sys.path.insert(0, r'${BIN_DIR.replace(/\\/g, "\\\\")}')
try:
    from mempalace_fast import search
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(0)
q = sys.stdin.read()
try:
    out = search(q, wing=${wingLiteral}, n=${n})
    results = out.get("results", [])
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(0)
hits = [
    {
        "similarity": round(r.get("similarity", 0), 3),
        "wing": r.get("wing", "") or "",
        "room": r.get("room", "") or "",
        "source": (r.get("source_file", "") or "").split("\\\\")[-1][:60],
        "text": (r.get("text", "") or "")[:500],
    }
    for r in results
]
print(json.dumps(hits))
`;
    const proc = spawn(python, ["-X", "utf8", "-c", code], {
      env: { ...process.env, PYTHONIOENCODING: "utf8" },
      shell: false,
      windowsHide: true,
    });

    let stdout = "";
    let settled = false;
    const settle = (hits: Hit[]) => {
      if (settled) return;
      settled = true;
      resolve(hits);
    };

    proc.stdout.on("data", (d) => (stdout += d.toString()));
    proc.stdin.write(query);
    proc.stdin.end();
    proc.on("close", () => {
      try {
        const parsed = JSON.parse(stdout.trim() || "[]");
        if (Array.isArray(parsed)) return settle(parsed);
        settle([]);
      } catch {
        settle([]);
      }
    });
    proc.on("error", () => settle([]));

    setTimeout(() => {
      try {
        proc.kill();
      } catch {}
      settle([]);
    }, SPAWN_BUDGET_MS);
  });
}

async function runSearch(query: string, n: number, wing?: string): Promise<Hit[]> {
  const viaDaemon = await searchViaDaemon(query, n, wing);
  if (viaDaemon !== null) return viaDaemon;
  return searchViaSpawn(query, n, wing);
}

// ── Dedup + format ───────────────────────────────────────────────────────────
function hitKey(h: Hit): string {
  return `${h.wing}|${h.source}|${(h.text || "").slice(0, 120)}`;
}

function dedupeGroups(
  groups: Array<{ label: string; hits: Hit[] }>,
): Array<{ label: string; hits: Hit[] }> {
  const seen = new Set<string>();
  return groups
    .map(({ label, hits }) => {
      const kept: Hit[] = [];
      for (const h of hits) {
        const k = hitKey(h);
        if (seen.has(k)) continue;
        seen.add(k);
        kept.push(h);
      }
      return { label, hits: kept };
    })
    .filter((g) => g.hits.length > 0);
}

function formatContext(groups: Array<{ label: string; hits: Hit[] }>): string {
  if (!groups.length) return "";

  const sections: string[] = [];
  for (const { label, hits } of groups) {
    const bodies = hits.map((h, i) => {
      const loc = [h.wing, h.room].filter(Boolean).join("/");
      const head = `#${i + 1} [${loc}] ${h.source || "(inline)"} · sim=${h.similarity}`;
      return `${head}\n${h.text}`;
    });
    sections.push(`### ${label}\n\n${bodies.join("\n\n---\n\n")}`);
  }

  return [
    "<mempalace-context>",
    "Auto-retrieved drawers from MemPalace. Generic hits cover the broad prompt;",
    "domain hits pull deep context from wings matching the prompt's topic.",
    "Treat them as background — cite or use only if relevant. Source-of-truth is",
    "YourVault when they disagree.",
    "",
    sections.join("\n\n════════════════════════════\n\n"),
    "</mempalace-context>",
    "",
  ].join("\n");
}

function shouldSkip(event: InputEvent): boolean {
  if (event.source === "extension") return true;
  const text = (event.text || "").trim();
  if (text.length < MIN_PROMPT_CHARS) return true;
  if (text.startsWith("/")) return true;
  if (text.includes("<mempalace-context>")) return true;
  return false;
}

// ── Extension entry ──────────────────────────────────────────────────────────
export default function (pi: ExtensionAPI) {
  const DEBUG = process.env.PI_INJECTOR_DEBUG === "1";

  pi.on("input", async (event): Promise<InputEventResult> => {
    if (shouldSkip(event)) {
      if (DEBUG) process.stderr.write(`[PromptInjector] skip source=${event.source} len=${event.text?.length ?? 0}\n`);
      return { action: "continue" };
    }

    const t0 = Date.now();
    const wings = detectWings(event.text);

    // Fire generic + per-wing queries in parallel. Each returns Hit[] (possibly empty).
    // Parallel so total latency = slowest query, not sum of queries.
    const queryPromises: Promise<{ label: string; hits: Hit[] }>[] = [
      runSearch(event.text, GENERIC_N).then((hits) => ({ label: "Generic recall (top hits across all wings)", hits })),
      ...wings.map(({ wing, label }) =>
        runSearch(event.text, DOMAIN_N, wing).then((hits) => ({
          label: `Domain recall: ${label} (wing=${wing})`,
          hits,
        })),
      ),
    ];

    const settled = await Promise.all(queryPromises);
    const dt = Date.now() - t0;

    const groups = dedupeGroups(settled);
    const totalHits = groups.reduce((n, g) => n + g.hits.length, 0);

    if (DEBUG) {
      process.stderr.write(
        `[PromptInjector] dt=${dt}ms wings=[${wings.map((w) => w.wing).join(",")}] hits=${totalHits}\n`,
      );
    }

    if (!totalHits) return { action: "continue" };

    const block = formatContext(groups);
    if (DEBUG) process.stderr.write(`[PromptInjector] injecting ${block.length} chars\n`);
    return {
      action: "transform",
      text: `${block}\n${event.text}`,
      images: event.images,
    };
  });

  pi.on("session_start", async (_e, ctx) => {
    ctx.ui.notify(
      "Prompt context injector armed (MemPalace: generic top-3 + domain-aware top-5 per matched wing)",
      "info",
    );
  });
}
