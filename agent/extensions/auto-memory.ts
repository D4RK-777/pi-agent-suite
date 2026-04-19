/**
 * pi Auto-Memory Layer (unified with Claude Code's memory)
 *
 * Points at Claude Code's memory dir so pi and Claude share one memory index:
 *   ~/.claude/projects/<sanitized-cwd>/memory/MEMORY.md         (index)
 *   ~/.claude/projects/<sanitized-cwd>/memory/{type}_{slug}.md  (per-topic)
 *
 * Same frontmatter schema Claude uses. Four memory types: user, feedback,
 * project, reference. What pi learns via pi_remember also shows up in Claude's
 * next session; what Claude writes shows up in pi's.
 *
 * Registers two tools:
 *   pi_remember — write or update a memory
 *   pi_forget   — delete a memory
 *
 * Injection:
 *   on session_start, read MEMORY.md
 *   on before_agent_start, prepend a <pi-memory> block with index + bodies
 *
 * Budget: total injected memory capped at 12000 chars so index + Git context +
 * project CLAUDE.md don't collectively blow out the context window.
 */

import type { ExtensionAPI, BeforeAgentStartEvent, BeforeAgentStartEventResult } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";
import { mkdir, readdir, readFile, unlink, writeFile } from "fs/promises";
import { homedir } from "os";
import { join } from "path";

// Canonical memory path = Claude Code's memory dir. PI_MEMORY_DIR env var
// overrides for advanced users (e.g. to run pi in isolation during testing).
// Claude Code sanitizes the project path into a directory name (replaces separators with "-").
// Set PI_MEMORY_DIR to point at your Claude memory folder, or leave unset to use ~/.pi/memory/.
const MEMORY_DIR = process.env.PI_MEMORY_DIR
  || join(homedir(), ".pi", "memory");
const INDEX_FILE = join(MEMORY_DIR, "MEMORY.md");
const MAX_INJECT_CHARS = 12000;

type MemoryType = "user" | "feedback" | "project" | "reference";
const VALID_TYPES: MemoryType[] = ["user", "feedback", "project", "reference"];

function slugify(s: string): string {
  return s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .slice(0, 60);
}

function fileNameFor(type: MemoryType, name: string): string {
  return `${type}_${slugify(name)}.md`;
}

async function ensureDir() {
  await mkdir(MEMORY_DIR, { recursive: true });
}

async function readIndex(): Promise<string> {
  try {
    return await readFile(INDEX_FILE, "utf8");
  } catch {
    return "";
  }
}

async function listMemoryFiles(): Promise<string[]> {
  try {
    const all = await readdir(MEMORY_DIR);
    return all.filter((f) => f.endsWith(".md") && f !== "MEMORY.md").sort();
  } catch {
    return [];
  }
}

async function buildInjectionBlock(): Promise<string> {
  const index = await readIndex();
  const files = await listMemoryFiles();
  if (!index.trim() && files.length === 0) return "";

  // Load each memory file, assemble index + bodies, cap total size.
  const bodies: string[] = [];
  let totalChars = 0;
  for (const f of files) {
    try {
      const content = await readFile(join(MEMORY_DIR, f), "utf8");
      const piece = `\n--- ${f} ---\n${content.trim()}\n`;
      if (totalChars + piece.length > MAX_INJECT_CHARS - 500) {
        bodies.push(`\n[… more memories truncated, total ${files.length} files]\n`);
        break;
      }
      bodies.push(piece);
      totalChars += piece.length;
    } catch {
      // skip unreadable
    }
  }

  return [
    "<pi-memory>",
    "Cross-session memory. Use these to stay coherent with what you already know about the user,",
    "their feedback, ongoing projects, and external references. Update via pi_remember / pi_forget.",
    "",
    "# INDEX",
    index.trim() || "(empty)",
    "",
    "# MEMORIES",
    bodies.join("\n"),
    "</pi-memory>",
  ].join("\n");
}

async function upsertMemory(
  type: MemoryType,
  name: string,
  description: string,
  body: string,
): Promise<{ file: string; action: "created" | "updated" }> {
  await ensureDir();
  const filename = fileNameFor(type, name);
  const filepath = join(MEMORY_DIR, filename);

  const frontmatter = [
    "---",
    `name: ${name}`,
    `description: ${description.replace(/\n/g, " ").trim()}`,
    `type: ${type}`,
    `updated: ${new Date().toISOString().slice(0, 10)}`,
    "---",
    "",
  ].join("\n");

  const fileContent = frontmatter + body.trim() + "\n";

  let action: "created" | "updated" = "created";
  try {
    await readFile(filepath, "utf8");
    action = "updated";
  } catch {
    // didn't exist → created
  }
  await writeFile(filepath, fileContent, "utf8");

  // Update index — idempotent.
  const existingIndex = await readIndex();
  const indexLine = `- [${name}](${filename}) — ${description.replace(/\n/g, " ").slice(0, 120)}`;
  const pattern = new RegExp(`^- \\[.*?\\]\\(${filename.replace(/\./g, "\\.")}\\).*$`, "m");

  let nextIndex: string;
  if (pattern.test(existingIndex)) {
    nextIndex = existingIndex.replace(pattern, indexLine);
  } else {
    nextIndex = (existingIndex.trim() ? existingIndex.trim() + "\n" : "") + indexLine + "\n";
  }
  await writeFile(INDEX_FILE, nextIndex, "utf8");
  return { file: filename, action };
}

async function forgetMemory(name: string): Promise<{ file: string; removed: boolean }> {
  const files = await listMemoryFiles();
  // Try all four types' slugified variants to find it.
  const slug = slugify(name);
  let target: string | null = null;
  for (const f of files) {
    if (f === `${slug}.md` || VALID_TYPES.some((t) => f === `${t}_${slug}.md`)) {
      target = f;
      break;
    }
  }
  if (!target) {
    // Fuzzy fallback: substring match on slug
    target = files.find((f) => f.includes(slug)) || null;
  }
  if (!target) return { file: "(none)", removed: false };

  try {
    await unlink(join(MEMORY_DIR, target));
  } catch {
    return { file: target, removed: false };
  }
  const existingIndex = await readIndex();
  const pattern = new RegExp(`^- \\[.*?\\]\\(${target.replace(/\./g, "\\.")}\\).*$\\n?`, "m");
  const nextIndex = existingIndex.replace(pattern, "");
  await writeFile(INDEX_FILE, nextIndex, "utf8");
  return { file: target, removed: true };
}

export default function (pi: ExtensionAPI) {
  let cachedBlock = "";

  async function refresh() {
    cachedBlock = await buildInjectionBlock();
  }

  pi.on("session_start", async (_event, ctx) => {
    await ensureDir();
    // Seed MEMORY.md if missing so the file exists and future writes don't race.
    try {
      await readFile(INDEX_FILE, "utf8");
    } catch {
      await writeFile(
        INDEX_FILE,
        "# pi memory index\n\n(Memories appear here as pi_remember is called.)\n",
        "utf8",
      );
    }
    await refresh();
    if (cachedBlock) {
      ctx.ui.notify("pi auto-memory loaded", "info");
    }
  });

  pi.on("before_agent_start", (_event: BeforeAgentStartEvent): BeforeAgentStartEventResult | void => {
    if (!cachedBlock) return;
    return { systemPrompt: cachedBlock };
  });

  const readOnly = process.env.PI_AUTO_MEMORY_READONLY === "1";

  pi.registerTool({
    name: "pi_remember",
    label: "pi remember",
    description:
      "Save a cross-session memory. Types: user (who they are), feedback (corrections/validations with Why+How), " +
      "project (current work facts), reference (pointers to external systems). " +
      "Body should be self-contained markdown. Writes to ~/.pi/memory/ and updates MEMORY.md index.",
    promptGuidelines: [
      "Call pi_remember when the user reveals a durable fact: role, preference, standing correction, project decision, or external resource pointer.",
      "Include a **Why:** and **How to apply:** line for `feedback` and `project` memories so future-you can judge edge cases.",
      "Do NOT save things derivable from code, git log, or vault files — those belong elsewhere.",
      "Prefer updating an existing memory (same `name`) over creating near-duplicates.",
    ],
    parameters: Type.Object({
      type: Type.Union([Type.Literal("user"), Type.Literal("feedback"), Type.Literal("project"), Type.Literal("reference")], {
        description: "Memory category.",
      }),
      name: Type.String({ description: "Short slug-friendly name. Becomes the filename." }),
      description: Type.String({ description: "One-line description — used in the index to decide relevance later." }),
      body: Type.String({
        description:
          "Full memory content. For feedback/project, include **Why:** and **How to apply:** lines so future-you can judge edge cases.",
      }),
    }),
    async execute(_toolCallId, params) {
      if (readOnly) {
        return {
          content: [{ type: "text", text: "Refused: PI_AUTO_MEMORY_READONLY=1 (likely a sub-agent context). Memory writes are disabled here." }],
          details: { refused: true, reason: "readonly" },
          isError: true,
        };
      }
      const result = await upsertMemory(params.type, params.name, params.description, params.body);
      await refresh();
      return {
        content: [
          {
            type: "text",
            text: `Memory ${result.action}: ${result.file}\nNext session will see it in <pi-memory>.`,
          },
        ],
        details: { file: result.file, action: result.action },
      };
    },
  });

  pi.registerTool({
    name: "pi_forget",
    label: "pi forget",
    description:
      "Delete a memory by name. Use when a memory is obsolete or wrong. " +
      "Also removes the entry from MEMORY.md.",
    promptGuidelines: [
      "Call pi_forget when a remembered fact becomes stale, wrong, or the user asks you to forget it.",
      "Prefer pi_remember (which overwrites) if the memory is updatable — only pi_forget for truly defunct entries.",
    ],
    parameters: Type.Object({
      name: Type.String({ description: "Name of the memory to remove (the 'name' used with pi_remember)." }),
    }),
    async execute(_toolCallId, params) {
      if (readOnly) {
        return {
          content: [{ type: "text", text: "Refused: PI_AUTO_MEMORY_READONLY=1 (sub-agent context). Memory deletions are disabled here." }],
          details: { refused: true, reason: "readonly" },
          isError: true,
        };
      }
      const result = await forgetMemory(params.name);
      await refresh();
      return {
        content: [
          {
            type: "text",
            text: result.removed ? `Removed ${result.file}` : `No memory matched '${params.name}'`,
          },
        ],
        details: result,
      };
    },
  });
}
