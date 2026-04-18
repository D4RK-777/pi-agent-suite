/**
 * Plan Mode for pi — Opus-style plan → approve → execute
 *
 * Registers `pi_present_plan` which the model uses for complex / ambiguous /
 * high-blast-radius tasks. The tool renders the plan in the UI and requests
 * confirmation before pi proceeds with implementation.
 *
 * Mirrors Claude Code's ExitPlanMode pattern but adapted to pi's tool system
 * (pi doesn't have a native plan-mode state, so we emulate via a tool that
 * asks the user to approve, then the model decides whether to execute).
 *
 * When to use it:
 *   - Multi-step refactors touching multiple files
 *   - Architectural decisions with irreversible consequences
 *   - Tasks where "let me just try it" could cause harm
 *
 * When NOT to use it:
 *   - Simple reads, lookups, single-line edits
 *   - Questions (answer directly — no plan needed)
 *   - Tasks the user clearly wants executed immediately ("just do X")
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";

export default function (pi: ExtensionAPI) {
  pi.registerTool({
    name: "pi_present_plan",
    label: "Present plan for approval",
    description:
      "Present an implementation plan to the user and request their approval BEFORE executing. " +
      "Use for complex multi-step tasks, architectural changes, or high-blast-radius work where " +
      "getting the approach right matters more than raw speed. Skip for simple reads, lookups, " +
      "or when the user has clearly said 'just do it'.",
    promptGuidelines: [
      "Call pi_present_plan BEFORE starting a multi-step implementation or a task with irreversible consequences.",
      "The plan should state: (1) the goal, (2) the approach, (3) the files/areas you'll touch, (4) assumptions, (5) what could go wrong.",
      "Do NOT call this for simple questions, single-file edits, or tasks the user asked you to 'just do'.",
      "After presenting, WAIT for the user's response. Do not start executing based on your own plan — they may want to revise.",
      "If the user approves, execute. If they redirect, adjust the plan and present again OR proceed with their revised direction.",
    ],
    parameters: Type.Object({
      goal: Type.String({
        description: "One-sentence statement of what the user actually wants achieved.",
      }),
      approach: Type.String({
        description: "2-4 sentences describing HOW you'll do it. Include the key decisions.",
      }),
      steps: Type.Array(
        Type.String({ description: "One step. Imperative form: 'Create X', 'Modify Y', 'Run Z'." }),
        { description: "Ordered list of concrete steps. Keep each step surgical and verifiable." },
      ),
      files_touched: Type.Optional(
        Type.Array(Type.String(), {
          description: "Specific file paths you expect to create, modify, or delete.",
        }),
      ),
      assumptions: Type.Optional(
        Type.Array(Type.String(), {
          description: "Things you're assuming that the user could correct. Be explicit.",
        }),
      ),
      risks: Type.Optional(
        Type.Array(Type.String(), {
          description: "What could go wrong. Include reversibility and blast radius.",
        }),
      ),
    }),
    async execute(_toolCallId, params, _signal, _onUpdate, ctx) {
      const lines: string[] = [];
      lines.push("## Proposed Plan");
      lines.push("");
      lines.push(`**Goal:** ${params.goal}`);
      lines.push("");
      lines.push(`**Approach:** ${params.approach}`);
      lines.push("");
      lines.push("**Steps:**");
      params.steps.forEach((s, i) => lines.push(`${i + 1}. ${s}`));
      lines.push("");

      if (params.files_touched?.length) {
        lines.push("**Files touched:**");
        for (const f of params.files_touched) lines.push(`- \`${f}\``);
        lines.push("");
      }
      if (params.assumptions?.length) {
        lines.push("**Assumptions:**");
        for (const a of params.assumptions) lines.push(`- ${a}`);
        lines.push("");
      }
      if (params.risks?.length) {
        lines.push("**Risks:**");
        for (const r of params.risks) lines.push(`- ${r}`);
        lines.push("");
      }
      lines.push("---");
      lines.push("Reply **'approved'** / **'go ahead'** to execute, or describe what you'd change.");

      const body = lines.join("\n");

      if (ctx.hasUI) {
        ctx.ui.notify("Plan presented — awaiting your approval", "info");
      }

      return {
        content: [{ type: "text", text: body }],
        details: {
          plan_steps: params.steps.length,
          files_touched: params.files_touched?.length || 0,
        },
      };
    },
  });
}
