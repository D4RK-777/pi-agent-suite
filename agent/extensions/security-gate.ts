/**
 * PreToolUse Security Gate
 *
 * Intercepts `tool_call` events and blocks dangerous operations before they run.
 * Pattern lifted from disler/claude-code-hooks-mastery, adapted for pi's event API
 * and this user's specific doctrine (OmegaD4rkMynd/raw/ is immutable, ShadowVault
 * is off-limits, etc).
 *
 * Philosophy:
 *   - Block only things that are *destructive or privacy-sensitive*, not annoying.
 *   - Always include a clear `reason` so the agent can self-correct.
 *   - Never block reads — those are always safe in this setup.
 *   - Keep rules tiny and auditable; this file is security-critical.
 *
 * If you need to bypass a rule intentionally, run the raw shell command in a
 * terminal outside pi — don't weaken the gate.
 */

import type { ExtensionAPI, ToolCallEvent, ToolCallEventResult } from "@mariozechner/pi-coding-agent";

interface Rule {
  name: string;
  toolMatch: (toolName: string) => boolean;
  check: (input: any) => { block: boolean; reason?: string };
}

// Regexes live at module scope so the matching cost is negligible.
const RX = {
  // rm -rf on anything that looks like a filesystem root, home dir, or user profile.
  rmRfRoot: /\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r|--recursive\s+--force|--force\s+--recursive)\s+(\/|~|\$HOME|C:[\\/]|%USERPROFILE%)(\s|$)/i,
  // Writing to or reading from OmegaD4rkMynd\raw\... (vault immutable rule).
  vaultRaw: /[\\/]OmegaD4rkMynd[\\/]raw[\\/]/i,
  // ShadowVault is off-limits per user doctrine unless they explicitly ask.
  shadowVault: /[\\/]ShadowVault[\\/]/i,
  // .env file paths — we don't want credentials leaking into model context.
  envFile: /(^|[\\/])\.env(\.[a-z]+)?$/i,
  // git push --force to main/master — permissible only with explicit user ask.
  gitForcePushProtected: /\bgit\s+push\s+(-[a-zA-Z]*f[a-zA-Z]*|--force(-with-lease)?)\s+.*\b(main|master)\b/i,
  // git reset --hard — too easy to lose work.
  gitResetHard: /\bgit\s+reset\s+(--hard|-[a-zA-Z]*h[a-zA-Z]*)/i,
  // git commit --no-verify — bypasses hooks; explicit ask required.
  gitNoVerify: /\bgit\s+(commit|push|merge|rebase)\s+.*--no-verify/i,
  // git config modifications — Claude Code convention: never modify.
  gitConfigWrite: /\bgit\s+config\s+(?!--get|--list|-l\b)/i,
  // curl/wget uploading a file (likely exfiltration pattern if triggered on user data).
  curlUpload: /\b(curl|wget|Invoke-WebRequest|iwr)\b.*(-F\s+|--data-binary\s+@|--upload-file|-T\s+)/i,
};

/** Extract the bash command string regardless of input shape (built-in vs custom). */
function readBashCommand(input: any): string {
  if (!input) return "";
  // Built-in bash tool uses `command`. Custom tools may wrap differently.
  return String(input.command ?? input.cmd ?? "");
}

/** Extract a filesystem path from write/edit/read inputs. */
function readPath(input: any): string {
  return String(input?.path ?? input?.file_path ?? input?.target ?? "");
}

const RULES: Rule[] = [
  {
    name: "rm-rf-root",
    toolMatch: (t) => t === "bash",
    check: (input) => {
      const cmd = readBashCommand(input);
      if (RX.rmRfRoot.test(cmd)) {
        return {
          block: true,
          reason:
            "Blocked rm -rf targeting a filesystem root, home, or user profile. " +
            "If this is intentional, run it manually in a terminal — not through pi.",
        };
      }
      return { block: false };
    },
  },
  {
    name: "vault-raw-immutable",
    toolMatch: (t) => t === "bash" || t === "write" || t === "edit",
    check: (input) => {
      const path = readPath(input);
      const cmd = readBashCommand(input);
      // Block write/edit tools unconditionally when the target path is under raw/.
      if (path && RX.vaultRaw.test(path)) {
        return {
          block: true,
          reason:
            "Blocked write to OmegaD4rkMynd/raw/. That folder is immutable by doctrine — " +
            "file into wiki/, decisions/, or patterns/ instead per the vault CLAUDE.md.",
        };
      }
      if (cmd && RX.vaultRaw.test(cmd)) {
        // Bash: allow pure readers (cat/type/less/more/head/tail/bat/Get-Content/rg/grep/find/ls/stat/file/wc).
        // Anything else that mentions raw/ is almost certainly a write (cp, mv, echo>, tee, Set-Content, rm, sed -i, …).
        const pureReader = /^\s*(cat|type|less|more|head|tail|bat|Get-Content|rg|grep|find|ls|dir|stat|file|wc|diff|md5sum|sha\d+sum|CertUtil)\b/i;
        if (!pureReader.test(cmd)) {
          return {
            block: true,
            reason:
              "Blocked bash command that writes to OmegaD4rkMynd/raw/. That folder is immutable. " +
              "Only read-only commands (cat/type/rg/grep/head/tail/ls/diff/etc.) may touch raw/.",
          };
        }
      }
      return { block: false };
    },
  },
  {
    name: "shadowvault-off-limits",
    toolMatch: (t) => t === "write" || t === "edit",
    check: (input) => {
      if (RX.shadowVault.test(readPath(input))) {
        return {
          block: true,
          reason:
            "Blocked write to ShadowVault — user's personal scratch vault is off-limits " +
            "unless they explicitly ask. Ask first or write to OmegaD4rkMynd.",
        };
      }
      return { block: false };
    },
  },
  {
    name: "env-file-read",
    toolMatch: (t) => t === "read" || t === "bash",
    check: (input) => {
      const path = readPath(input);
      const cmd = readBashCommand(input);
      const hit = RX.envFile.test(path) || /\b(cat|type|less|more|head|tail|bat|Get-Content)\b[^\n]*\.env\b/i.test(cmd);
      if (hit) {
        return {
          block: true,
          reason:
            "Blocked .env file access. Credentials shouldn't enter the model's context. " +
            "If you need a specific value, ask the user to paste just that variable.",
        };
      }
      return { block: false };
    },
  },
  {
    name: "git-force-push-protected",
    toolMatch: (t) => t === "bash",
    check: (input) => {
      if (RX.gitForcePushProtected.test(readBashCommand(input))) {
        return {
          block: true,
          reason:
            "Blocked force-push to main/master. Use a feature branch, or if you really " +
            "must, ask the user for explicit confirmation and run it manually.",
        };
      }
      return { block: false };
    },
  },
  {
    name: "git-reset-hard",
    toolMatch: (t) => t === "bash",
    check: (input) => {
      if (RX.gitResetHard.test(readBashCommand(input))) {
        return {
          block: true,
          reason:
            "Blocked `git reset --hard`. Too easy to lose uncommitted work. " +
            "Use `git stash` or `git checkout -- <file>` for targeted reverts, or ask the user to confirm.",
        };
      }
      return { block: false };
    },
  },
  {
    name: "git-no-verify",
    toolMatch: (t) => t === "bash",
    check: (input) => {
      if (RX.gitNoVerify.test(readBashCommand(input))) {
        return {
          block: true,
          reason:
            "Blocked --no-verify. Skipping hooks masks real problems; fix the hook failure instead.",
        };
      }
      return { block: false };
    },
  },
  {
    name: "git-config-write",
    toolMatch: (t) => t === "bash",
    check: (input) => {
      if (RX.gitConfigWrite.test(readBashCommand(input))) {
        return {
          block: true,
          reason:
            "Blocked git config mutation. User's git config is never modified by the agent.",
        };
      }
      return { block: false };
    },
  },
];

// Regex evaluation is ~microsecond-fast on normal inputs but can backtrack
// pathologically on very long strings. Cap input length before running rules
// so a rogue 500KB bash command can't stall the event loop. 50KB is far more
// than any reasonable command + comfortably fits ripgrep's max regex line length.
const MAX_INPUT_CHARS_FOR_RULES = 50_000;

export default function (pi: ExtensionAPI) {
  const blockCounts = new Map<string, number>();

  pi.on("tool_call", (event: ToolCallEvent, ctx): ToolCallEventResult | void => {
    // DoS guard: skip regex checks on absurdly long inputs. Any real command
    // that hits this is either programmatically generated noise or an attempt
    // to evade the gate — either way, safer to block outright than to scan.
    const input = (event as any).input;
    const rawLen = input ? JSON.stringify(input).length : 0;
    if (rawLen > MAX_INPUT_CHARS_FOR_RULES) {
      blockCounts.set("oversize-input", (blockCounts.get("oversize-input") || 0) + 1);
      const reason = `Blocked oversize tool input (${rawLen} chars > ${MAX_INPUT_CHARS_FOR_RULES}). If this is legitimate, split the command or stream the data through a file.`;
      if (ctx.hasUI) {
        ctx.ui.notify(`[security-gate] oversize-input: ${reason}`, "warning");
      }
      return { block: true, reason };
    }

    for (const rule of RULES) {
      if (!rule.toolMatch(event.toolName)) continue;
      const verdict = rule.check(input);
      if (verdict.block) {
        blockCounts.set(rule.name, (blockCounts.get(rule.name) || 0) + 1);
        if (ctx.hasUI) {
          ctx.ui.notify(`[security-gate] ${rule.name}: ${verdict.reason}`, "warning");
        }
        return { block: true, reason: verdict.reason };
      }
    }
  });

  pi.on("session_start", (_event, ctx) => {
    ctx.ui.notify(`Security gate armed (${RULES.length} rules)`, "info");
  });

  pi.on("session_shutdown", (_event, ctx) => {
    if (blockCounts.size === 0) return;
    const summary = Array.from(blockCounts.entries())
      .map(([rule, n]) => `${rule}=${n}`)
      .join(", ");
    if (ctx.hasUI) {
      ctx.ui.notify(`Security gate blocked: ${summary}`, "info");
    }
  });
}
