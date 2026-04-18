/**
 * Project CLAUDE.md Auto-Discovery
 *
 * On session_start, walk cwd upward looking for project-level instructions,
 * cache them, and inject into every turn's system prompt via before_agent_start.
 *
 * Discovery order (first found per filename wins at each level):
 *   .pi/CLAUDE.md  → .pi/AGENTS.md  → CLAUDE.md  → AGENTS.md
 *
 * We walk up to 8 levels and stop at the first filesystem root we hit.
 * We collect ALL findings on the way up (closer-to-cwd wins on dupes) and
 * chain them oldest-ancestor-first so the closest scope is most recent in the
 * prompt — matching Claude Code's project-local-overrides-global behavior.
 *
 * Cached once per session_start; re-reads only on /reload.
 */

import type { ExtensionAPI, BeforeAgentStartEvent, BeforeAgentStartEventResult } from "@mariozechner/pi-coding-agent";
import { readFile, stat } from "fs/promises";
import { dirname, join, parse } from "path";

const CANDIDATE_FILES = [".pi/CLAUDE.md", ".pi/AGENTS.md", "CLAUDE.md", "AGENTS.md"];
const MAX_WALK_DEPTH = 8;
// Cap total injected chars so we don't blow the context window if someone
// leaves a 50k-word CLAUDE.md somewhere up the tree.
const MAX_TOTAL_CHARS = 16000;

// NOTE: We intentionally do NOT load ~/.claude/CLAUDE.md (Claude Code's global
// doctrine) because it's heavily Obsidian-tool-routed and pi doesn't have those
// tools. Pi's doctrine lives in PI_KNOWLEDGE_SYSTEM.md (appended via settings)
// plus shared auto-memory. The user-level rules that matter (quality bars, brand,
// verbatim doctrine) are already in PI_KNOWLEDGE_SYSTEM.md and memory files.

interface Found {
  path: string;
  depth: number; // 0 = cwd, 1 = parent, ...
  content: string;
}

async function readIfExists(p: string): Promise<string | null> {
  try {
    const s = await stat(p);
    if (!s.isFile()) return null;
    return await readFile(p, "utf8");
  } catch {
    return null;
  }
}

async function walkUp(cwd: string): Promise<Found[]> {
  const found: Found[] = [];
  const seenContent = new Set<string>(); // dedupe by content hash-ish

  let dir = cwd;
  const root = parse(dir).root;

  for (let depth = 0; depth < MAX_WALK_DEPTH; depth++) {
    for (const candidate of CANDIDATE_FILES) {
      const full = join(dir, candidate);
      const content = await readIfExists(full);
      if (!content) continue;
      // Simple dedupe — same first 200 chars.
      const key = content.slice(0, 200);
      if (seenContent.has(key)) continue;
      seenContent.add(key);
      found.push({ path: full, depth, content });
    }
    const parent = dirname(dir);
    if (parent === dir || dir === root) break;
    dir = parent;
  }
  return found;
}

function buildSystemPromptBlock(found: Found[]): string {
  if (!found.length) return "";
  // Sort farthest-ancestor first so closer-to-cwd ends up latest in the prompt.
  const ordered = [...found].sort((a, b) => b.depth - a.depth);
  const chunks: string[] = [];
  let totalChars = 0;
  for (const f of ordered) {
    const scope = f.depth === 0 ? "cwd" : `${f.depth} levels up`;
    const header = `\n--- ${f.path} (${scope}) ---\n`;
    const piece = header + f.content;
    if (totalChars + piece.length > MAX_TOTAL_CHARS) {
      chunks.push(header + `[truncated — file is ${f.content.length} chars, over budget]`);
      break;
    }
    chunks.push(piece);
    totalChars += piece.length;
  }
  return [
    "<project-instructions>",
    "The following CLAUDE.md / AGENTS.md files were discovered by walking up from the working directory.",
    "Treat these as authoritative for this project. Closer scopes override farther ones.",
    chunks.join("\n"),
    "</project-instructions>",
  ].join("\n");
}

export default function (pi: ExtensionAPI) {
  let cachedBlock = "";
  let cachedFrom = "";

  async function refresh(cwd: string) {
    const found = await walkUp(cwd);
    cachedBlock = buildSystemPromptBlock(found);
    cachedFrom = cwd;
    return found.length;
  }

  pi.on("session_start", async (_event, ctx) => {
    const count = await refresh(ctx.cwd);
    if (count > 0) {
      ctx.ui.notify(`Project CLAUDE.md loader: found ${count} instruction file(s)`, "info");
    }
  });

  pi.on("before_agent_start", (_event: BeforeAgentStartEvent, ctx): BeforeAgentStartEventResult | void => {
    // Refresh lazily if cwd drifted mid-session (rare, but /cd could).
    if (cachedFrom !== ctx.cwd) {
      // Fire-and-forget refresh; next turn will use fresh data.
      void refresh(ctx.cwd);
    }
    if (!cachedBlock) return;
    // Chain-append: pi chains systemPrompt values across extensions, so returning
    // just our block won't replace the existing one — pi adds ours on top.
    return { systemPrompt: cachedBlock };
  });
}
