/**
 * Adaptive Error Recovery — 3-strikes-and-pivot
 *
 * Mirrors Claude Code's adaptive-error-recovery skill at the harness level.
 * When a tool call fails with the same signature repeatedly, inject a
 * system-prompt override telling the model to stop and pivot.
 *
 * Without this, pi sometimes loops — same tool, same args, same error — wasting
 * tokens and user time. This watches tool_execution_end, tracks failure
 * signatures, and after 3 consecutive strikes injects a STOP-AND-PIVOT
 * notice into the next before_agent_start.
 *
 * Scope: per-session (resets on session_start).
 */

import type { ExtensionAPI, BeforeAgentStartEvent, BeforeAgentStartEventResult, ToolExecutionEndEvent, ToolCallEvent, ToolCallEventResult } from "@mariozechner/pi-coding-agent";

const STRIKE_LIMIT = 3;
const SIGNATURE_MAX_LEN = 120;

interface FailureTrack {
  signature: string;
  count: number;
  tool: string;
  lastSeen: number;
}

const ERROR_MARKERS = [
  /\bENOENT\b/,
  /\bEACCES\b/,
  /\bEPERM\b/,
  /\bEINVAL\b/,
  /\bETIMEDOUT\b/,
  /\bconnection refused\b/i,
  /\bno such file or directory\b/i,
  /\bpermission denied\b/i,
  /\bcommand not found\b/i,
  /\bfailed to\b/i,
  /\bcannot find\b/i,
  /\bunable to\b/i,
  /\berror:\s/i,
  /^\s*(Error|TypeError|ReferenceError|SyntaxError):/m,
  /\bHTTP (4\d\d|5\d\d)\b/,
  /\btraceback \(most recent call last\)/i,
];

function detectErrorContent(result: any): boolean {
  let text = "";
  if (result?.content && Array.isArray(result.content)) {
    for (const c of result.content) {
      if (c?.type === "text" && typeof c.text === "string") text += c.text;
    }
  } else if (typeof result === "string") {
    text = result;
  }
  if (!text || text.length > 5000) return false; // too big = probably real content
  return ERROR_MARKERS.some(rx => rx.test(text));
}

function failureSignature(toolName: string, result: any): string {
  // Extract a stable error signature from the result.
  // We want "same tool + same error shape" to collide, even if the exact
  // filename / line differs.
  let text = "";
  if (result?.content && Array.isArray(result.content)) {
    for (const c of result.content) {
      if (c?.type === "text" && typeof c.text === "string") {
        text += c.text;
      }
    }
  } else if (typeof result === "string") {
    text = result;
  }

  // Strip volatile bits: timestamps, paths, line numbers, hashes.
  const normalized = text
    .replace(/\d{4}-\d{2}-\d{2}T[\d:.]+Z?/g, "<ts>")
    .replace(/[A-Z]:\\[^\s"']+/g, "<path>")
    .replace(/\/[\w./\-]+/g, "<path>")
    .replace(/\b0x[0-9a-f]+\b/gi, "<hex>")
    .replace(/\bline \d+\b/g, "line <n>")
    .replace(/\b\d{3,}\b/g, "<n>")
    .slice(0, SIGNATURE_MAX_LEN)
    .trim();

  return `${toolName}::${normalized}`;
}

function argSignature(args: any): string {
  try {
    const s = JSON.stringify(args || {});
    return s
      .replace(/[A-Z]:\\\\[^"']+/g, "<path>")
      .replace(/\/[\w./\-]+/g, "<path>")
      .slice(0, 200);
  } catch {
    return "";
  }
}

export default function (pi: ExtensionAPI) {
  let current: FailureTrack | null = null;
  let pivotPending = false;
  // Track recent tool calls (tool + arg signature) so we can block mid-turn retries.
  const recentCalls: Array<{ tool: string; argSig: string; ts: number }> = [];

  pi.on("session_start", () => {
    current = null;
    pivotPending = false;
    recentCalls.length = 0;
  });

  // Block mid-turn: if the model keeps calling the same (tool, args) after 3
  // failures in a row, refuse the 4th. This happens BEFORE the tool runs, so
  // the model gets a clear signal to pivot within the same turn.
  pi.on("tool_call", (event: ToolCallEvent): ToolCallEventResult | void => {
    if (!current || current.count < STRIKE_LIMIT) return;
    const toolName = (event as any).toolName || "unknown";
    if (toolName !== current.tool) return;
    // Only block if we're still in the failing streak (reset on success in tool_execution_end).
    return {
      block: true,
      reason:
        `Adaptive recovery: \`${current.tool}\` has failed ${current.count}× in a row with the same error shape. ` +
        `Stop retrying. Diagnose the root cause, try a different tool/approach, or tell the user what you've tried and ask for guidance. ` +
        `Do NOT fake success.`,
    };
  });

  pi.on("tool_execution_end", (event: ToolExecutionEndEvent) => {
    const toolName = event.toolName || "unknown";

    // Some pi tools return errors as content without setting isError=true
    // (e.g. file-not-found returns {content:[{type:"text",text:"ENOENT..."}]}).
    // Detect both explicit isError AND error-shaped content.
    const looksLikeError = !event.isError && detectErrorContent(event.result);

    if (!event.isError && !looksLikeError) {
      // Real success — reset the streak.
      current = null;
      return;
    }

    const sig = failureSignature(toolName, event.result);

    if (current && current.signature === sig) {
      current.count++;
      current.lastSeen = Date.now();
      if (current.count >= STRIKE_LIMIT) {
        pivotPending = true;
      }
    } else {
      current = { signature: sig, count: 1, tool: toolName, lastSeen: Date.now() };
    }
  });

  pi.on("before_agent_start", (_e: BeforeAgentStartEvent): BeforeAgentStartEventResult | void => {
    if (!pivotPending || !current) return;

    // Build a clear pivot notice. Single-shot — reset after injection so we
    // don't keep nagging once the model has been told.
    const notice = [
      "<pivot-required>",
      `⚠ Tool \`${current.tool}\` has failed ${current.count}× with the same error signature.`,
      "",
      "**Stop repeating this approach.** Do NOT retry the same tool call. Instead:",
      "- Read the actual error carefully. What's it actually telling you?",
      "- Try a DIFFERENT approach: different tool, different arguments, or different strategy entirely.",
      "- If you're stuck on what to try next, tell the user what you've attempted and ask for guidance.",
      "- Do NOT fake success. If the thing can't be done the way you've been trying, say so.",
      "</pivot-required>",
    ].join("\n");

    pivotPending = false;
    current = null;

    return { systemPrompt: notice };
  });
}
