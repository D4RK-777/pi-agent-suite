/**
 * SessionStart Git Context Injector
 *
 * On session_start, gather a compact snapshot of the working tree:
 *   - current branch + upstream divergence
 *   - git status short
 *   - last 5 commits
 *   - any TODO(claude) / FIXME(claude) markers in tracked files
 *
 * Inject that as an additional system prompt chunk via before_agent_start so the
 * model sees it from turn 1. Solves the "where was I?" cold-start problem.
 *
 * Budget: ~200ms. We run `git` in parallel, cap output, and fail silently if
 * we're not in a repo.
 */

import type { ExtensionAPI, BeforeAgentStartEvent, BeforeAgentStartEventResult } from "@mariozechner/pi-coding-agent";
import { spawn } from "child_process";

const GIT_TIMEOUT_MS = 1500;
const MAX_STATUS_LINES = 25;
const MAX_TODO_HITS = 15;

function runGit(cwd: string, args: string[]): Promise<string> {
  return new Promise((resolve) => {
    const proc = spawn("git", args, { cwd, shell: false, windowsHide: true });
    let stdout = "";
    let settled = false;
    const settle = (v: string) => {
      if (!settled) {
        settled = true;
        resolve(v);
      }
    };
    proc.stdout.on("data", (d) => (stdout += d.toString()));
    proc.on("close", () => settle(stdout));
    proc.on("error", () => settle(""));
    setTimeout(() => {
      try {
        proc.kill();
      } catch {}
      settle(stdout);
    }, GIT_TIMEOUT_MS);
  });
}

function runRg(cwd: string, args: string[]): Promise<string> {
  return new Promise((resolve) => {
    const proc = spawn("rg", args, { cwd, shell: false, windowsHide: true });
    let stdout = "";
    let settled = false;
    const settle = (v: string) => {
      if (!settled) {
        settled = true;
        resolve(v);
      }
    };
    proc.stdout.on("data", (d) => (stdout += d.toString()));
    proc.on("close", () => settle(stdout));
    proc.on("error", () => settle("")); // rg not installed → silent
    setTimeout(() => {
      try {
        proc.kill();
      } catch {}
      settle(stdout);
    }, GIT_TIMEOUT_MS);
  });
}

async function gatherContext(cwd: string): Promise<string> {
  // Quick probe: are we in a repo?
  const rev = await runGit(cwd, ["rev-parse", "--is-inside-work-tree"]);
  if (rev.trim() !== "true") return "";

  const [branch, ahead, statusRaw, logRaw, todoRaw] = await Promise.all([
    runGit(cwd, ["rev-parse", "--abbrev-ref", "HEAD"]),
    runGit(cwd, ["rev-list", "--left-right", "--count", "@{u}...HEAD"]),
    runGit(cwd, ["status", "--short", "--untracked-files=no"]),
    runGit(cwd, ["log", "-5", "--oneline", "--no-decorate"]),
    runRg(cwd, ["-n", "--no-heading", "(TODO|FIXME)\\(claude\\)", "--glob", "!node_modules", "--glob", "!.git"]),
  ]);

  const branchName = branch.trim() || "(detached)";
  let divergence = "";
  const aheadMatch = ahead.trim().split(/\s+/);
  if (aheadMatch.length === 2) {
    const [behind, aheadN] = aheadMatch;
    if (behind !== "0" || aheadN !== "0") {
      divergence = ` (ahead ${aheadN}, behind ${behind})`;
    }
  }

  const statusLines = statusRaw
    .split("\n")
    .filter((l) => l.trim())
    .slice(0, MAX_STATUS_LINES);
  const statusBlock = statusLines.length
    ? statusLines.join("\n") + (statusRaw.split("\n").filter((l) => l.trim()).length > MAX_STATUS_LINES ? "\n…" : "")
    : "(clean)";

  const logBlock = logRaw.trim() || "(no commits yet)";

  const todoLines = todoRaw
    .split("\n")
    .filter((l) => l.trim())
    .slice(0, MAX_TODO_HITS);
  const todoBlock = todoLines.length ? todoLines.join("\n") : "";

  const parts = [
    "<session-git-context>",
    `Branch: ${branchName}${divergence}`,
    "",
    "Status:",
    statusBlock,
    "",
    "Recent commits:",
    logBlock,
  ];
  if (todoBlock) {
    parts.push("", "TODO(claude) markers:", todoBlock);
  }
  parts.push("</session-git-context>");
  return parts.join("\n");
}

export default function (pi: ExtensionAPI) {
  let cachedBlock = "";
  let cachedFrom = "";
  // Debounce: at most one refresh in flight. Without this, rapid cwd drift in a
  // tight loop can spawn a wave of git/rg processes that pile up faster than
  // they can complete (5 processes per refresh × N turns). Skip if already in flight.
  let refreshInFlight = false;

  async function refresh(cwd: string) {
    if (refreshInFlight) return;
    refreshInFlight = true;
    try {
      cachedBlock = await gatherContext(cwd);
      cachedFrom = cwd;
    } catch {
      cachedBlock = "";
    } finally {
      refreshInFlight = false;
    }
  }

  pi.on("session_start", async (_event, ctx) => {
    await refresh(ctx.cwd);
    if (cachedBlock) {
      ctx.ui.notify("Session git context loaded", "info");
    }
  });

  pi.on("before_agent_start", (_event: BeforeAgentStartEvent, ctx): BeforeAgentStartEventResult | void => {
    if (cachedFrom !== ctx.cwd && !refreshInFlight) {
      void refresh(ctx.cwd);
    }
    if (!cachedBlock) return;
    return { systemPrompt: cachedBlock };
  });
}
