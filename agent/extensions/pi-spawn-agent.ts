/**
 * pi_spawn_agent — Subagent Emulation
 *
 * Pi has no native Task tool. This emulates Claude Code's Agent tool by spawning
 * a child `pi --print --no-session` process with a task-specific prompt.
 *
 * Use cases:
 *   - Research without polluting main context (web search, codebase exploration)
 *   - Parallel investigation ("check A and B and C independently")
 *   - Cheaper model routing (spawn workers on high-speed, keep lead on strong)
 *
 * Safety:
 *   - Depth guard via PI_SUBAGENT_DEPTH env var prevents infinite recursion.
 *   - Per-agent timeout prevents runaways.
 *   - Inherits the main agent's security-gate (child pi loads same extensions).
 *
 * Trade-offs honest:
 *   - Spawn cost: each child pays a full pi startup (~2–3s). For quick lookups
 *     this is overhead; reserve for meaningful research or long-running work.
 *   - No streaming: we block until the child exits and return all-at-once.
 *   - No tool-level parallelism guarantees — pi's scheduler decides whether
 *     multiple pi_spawn_agent calls in one turn run concurrently (depends on
 *     pi's ToolExecutionMode config).
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";
import { spawn } from "child_process";

const MAX_DEPTH = 1; // main spawns subagent; subagent cannot spawn further.
const DEFAULT_TIMEOUT_MS = 10 * 60 * 1000; // 10 minutes
const MAX_OUTPUT_CHARS = 60_000;

const SUBAGENT_SYSTEM_APPEND = `
# You are a pi sub-agent

You were spawned by a parent pi session to do focused work. Rules:
- You have no memory of the parent conversation — the prompt is self-contained.
- Your reply goes back to the parent as a single tool result. Be concise, specific, actionable.
- Cite exact file paths, line numbers, and commit SHAs — don't make claims the parent can't verify.
- Do NOT spawn further sub-agents. Your depth is capped.
- If the task is impossible or the premise is wrong, say so in your reply — don't fake success.
`;

/**
 * Resolve pi's actual JS entry point.
 *
 * On Windows, `npm install -g` creates a `.cmd` shim. Node.js (since 16, post
 * CVE-2024-27980) refuses to spawn .cmd/.bat files with shell:false — it throws
 * EINVAL instantly, which was silently breaking every sub-agent spawn. Calling
 * the shim with shell:true would work but requires fragile argument escaping
 * for multi-line system prompts.
 *
 * Cleanest fix: skip the shim. Spawn `node <pi-cli.js> ...` directly.
 * No shell, no escaping, no EINVAL.
 */
function piEntry(): { command: string; leadingArgs: string[] } {
  const override = process.env.PI_BIN_PATH;
  if (override) {
    // User override. If it's a .js file, spawn it via node; otherwise assume it's a real binary.
    if (override.endsWith(".js")) return { command: process.execPath, leadingArgs: [override] };
    return { command: override, leadingArgs: [] };
  }

  if (process.platform === "win32") {
    const jsPath = "C:\\Users\\chris\\AppData\\Roaming\\npm\\node_modules\\@mariozechner\\pi-coding-agent\\dist\\cli.js";
    return { command: process.execPath, leadingArgs: [jsPath] };
  }

  return { command: "pi", leadingArgs: [] };
}

interface SpawnResult {
  ok: boolean;
  stdout: string;
  stderr: string;
  exitCode: number | null;
  durationMs: number;
  truncated: boolean;
  timedOut: boolean;
}

function runChild(prompt: string, opts: { model?: string; timeoutMs: number; systemAppend: string }): Promise<SpawnResult> {
  return new Promise((resolve) => {
    const piArgs = ["--print", "--no-session", "--mode", "text", "--append-system-prompt", opts.systemAppend];
    if (opts.model) {
      piArgs.push("--model", opts.model);
    }

    const { command, leadingArgs } = piEntry();
    const args = [...leadingArgs, ...piArgs];

    const env = {
      ...process.env,
      PI_SUBAGENT_DEPTH: String((Number(process.env.PI_SUBAGENT_DEPTH) || 0) + 1),
      // Disable auto-memory write for subagents — they shouldn't update user memory.
      PI_AUTO_MEMORY_READONLY: "1",
    };

    const t0 = Date.now();
    const proc = spawn(command, args, {
      env,
      shell: false,
      windowsHide: true,
      stdio: ["pipe", "pipe", "pipe"],
    });

    let stdout = "";
    let stderr = "";
    let settled = false;
    let timedOut = false;

    const finish = (exitCode: number | null) => {
      if (settled) return;
      settled = true;
      const truncated = stdout.length > MAX_OUTPUT_CHARS;
      resolve({
        ok: exitCode === 0 && !timedOut,
        stdout: truncated ? stdout.slice(0, MAX_OUTPUT_CHARS) + "\n[...truncated]" : stdout,
        stderr: stderr.length > 4000 ? stderr.slice(-4000) : stderr,
        exitCode,
        durationMs: Date.now() - t0,
        truncated,
        timedOut,
      });
    };

    proc.stdout.on("data", (d) => {
      stdout += d.toString();
      // Hard cap to prevent memory blow-up on runaway children.
      if (stdout.length > MAX_OUTPUT_CHARS * 2) {
        try { proc.kill(); } catch {}
      }
    });
    proc.stderr.on("data", (d) => {
      stderr += d.toString();
    });
    proc.on("close", (code) => finish(code));
    proc.on("error", (err) => {
      stderr += "\n[spawn error] " + err.message;
      finish(-1);
    });

    const timer = setTimeout(() => {
      timedOut = true;
      try { proc.kill(); } catch {}
      setTimeout(() => finish(-2), 500); // grace period for cleanup
    }, opts.timeoutMs);

    // Send prompt via stdin so we don't have to escape it as an argv.
    try {
      proc.stdin.write(prompt);
      proc.stdin.end();
    } catch (err) {
      clearTimeout(timer);
      stderr += "\n[stdin write error] " + (err as Error).message;
      finish(-3);
    }

    proc.on("close", () => clearTimeout(timer));
  });
}

export default function (pi: ExtensionAPI) {
  const currentDepth = Number(process.env.PI_SUBAGENT_DEPTH) || 0;
  const atMaxDepth = currentDepth >= MAX_DEPTH;

  pi.registerTool({
    name: "pi_spawn_agent",
    label: "pi spawn agent",
    description:
      "Spawn a child pi agent to do focused work in an isolated context. Use for research, " +
      "parallel investigation, or any task where you'd rather not pollute the main conversation. " +
      "The child has its own MemPalace/Obsidian access but no memory of this conversation — " +
      "the prompt must be self-contained. Returns the child's final reply as the tool result. " +
      "NOT available in sub-agents (depth capped at 1).",
    promptGuidelines: [
      "Spawn sub-agents for: wide codebase exploration, web research, parallel independent investigations, or anything that would bloat main context with raw searches.",
      "Do NOT spawn for: simple file reads, single grep calls, or tasks where you already know the answer shape.",
      "The prompt must be SELF-CONTAINED — the sub-agent has zero memory of this conversation. Pass all relevant file paths, constraints, and what you've already tried.",
      "Launch multiple sub-agents in parallel (one message, multiple tool calls) when the subtasks are independent.",
      "Ask for a SHORT, SPECIFIC report — 'under 200 words' — so results don't blow your context when they return.",
    ],
    parameters: Type.Object({
      description: Type.String({
        description: "Short 3-5 word label describing what the sub-agent will do. Shown in UI.",
      }),
      prompt: Type.String({
        description:
          "The full self-contained task for the sub-agent. Include: goal, relevant file paths, " +
          "what's already been tried, and the expected output shape. Do not assume the sub-agent " +
          "knows anything about this conversation.",
      }),
      subagent_type: Type.Optional(
        Type.String({
          description:
            "Optional role hint appended to the sub-agent's system prompt. Common: 'researcher', 'explorer', 'reviewer', 'planner'.",
        }),
      ),
      model: Type.Optional(
        Type.String({
          description:
            "Optional model override, e.g. 'minimax/MiniMax-M2.7-highspeed'. Defaults to whatever pi is configured to use. " +
            "Route cheap subtasks to faster/cheaper models and keep lead on strong.",
        }),
      ),
      timeout_minutes: Type.Optional(
        Type.Number({
          description: "Per-spawn timeout in minutes (default 10, max 30).",
        }),
      ),
    }),
    async execute(_toolCallId, params, _signal, _onUpdate, ctx) {
      if (atMaxDepth) {
        return {
          content: [
            {
              type: "text",
              text: `[pi_spawn_agent] Refused: already at sub-agent depth ${currentDepth}. Sub-agents cannot spawn further sub-agents.`,
            },
          ],
          details: { refused: true, reason: "max_depth" },
        };
      }

      const timeoutMs = Math.min(
        Math.max((params.timeout_minutes || 10) * 60_000, 30_000),
        30 * 60_000,
      );

      const roleHint = params.subagent_type
        ? `\nRole: ${params.subagent_type}\n`
        : "";
      const systemAppend = SUBAGENT_SYSTEM_APPEND + roleHint;

      if (ctx.hasUI) {
        ctx.ui.notify(`[subagent] spawning: ${params.description}`, "info");
      }

      const result = await runChild(params.prompt, {
        model: params.model,
        timeoutMs,
        systemAppend,
      });

      const header = result.ok
        ? `[subagent done in ${result.durationMs}ms]`
        : `[subagent failed: exit=${result.exitCode} timedOut=${result.timedOut} dur=${result.durationMs}ms]`;

      const body = result.stdout.trim() || "(no output)";
      const stderrSuffix = result.stderr.trim()
        ? `\n\n--- stderr ---\n${result.stderr.trim()}`
        : "";

      return {
        content: [
          {
            type: "text",
            text: `${header}\n\n${body}${stderrSuffix}`,
          },
        ],
        details: {
          ok: result.ok,
          exitCode: result.exitCode,
          durationMs: result.durationMs,
          truncated: result.truncated,
          timedOut: result.timedOut,
          description: params.description,
        },
        isError: !result.ok,
      };
    },
  });

  pi.on("session_start", (_event, ctx) => {
    if (atMaxDepth) {
      ctx.ui.notify(`pi_spawn_agent disabled (sub-agent depth ${currentDepth})`, "warning");
    } else {
      ctx.ui.notify("pi_spawn_agent available (depth 0/1)", "info");
    }
  });
}
