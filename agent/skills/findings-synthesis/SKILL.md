---
name: findings-synthesis
description: >-
  Use when multiple reports, agent outputs, audit findings, or partial analyses need to be turned
  into one sharp executive picture with priorities, common root causes, and a credible next move.
  Triggers on \"synthesize this\", \"summarize the reports\", \"what matters most?\", \"turn this
  swarm into a plan\", or when many findings exist but the decision surface is still noisy.
trigger: synthesis, reports, swarm output, prioritization
tags:
  - synthesis
  - prioritization
  - reporting
  - planning
  - swarm
  - findings
---

# Findings Synthesis

## Purpose

Use this skill to compress many partial outputs into one clear decision-ready view.

This skill is for moments where the system already has signal, but the signal is scattered across
reports, agents, audits, or review notes. The goal is to reduce noise, expose the true priority
stack, and convert diffuse findings into action.

## When to Use

- A multi-agent audit produced many separate reports
- Several lanes surfaced overlapping risks or fixes
- The user wants the \"so what\" instead of another raw dump
- Findings need to be grouped into priorities, themes, and next steps
- A project has too many issues to tackle one by one without synthesis

## Rules

- Group by root cause, not just by file or report source.
- Distinguish critical blockers from valuable but deferrable cleanup.
- Collapse duplicates aggressively.
- Preserve severity and confidence; do not flatten all findings into the same weight.
- End with an execution-ready sequence, not just a summary.
- If the outputs conflict, say that directly instead of averaging them into mush.

## Workflow

1. Gather the inputs.
   - Reports, findings, agent outputs, review notes, or audit summaries.
2. Normalize the signal.
   - Identify duplicates, overlaps, contradictions, and recurring root causes.
3. Build the priority stack.
   - What blocks release, what weakens confidence, what is cleanup, what is optional.
4. Translate into action.
   - Turn the stack into a small number of concrete workstreams or next steps.
5. State residual uncertainty.
   - What still needs proof, validation, or deeper inspection?

## Expected Output

- synthesized executive summary
- grouped findings by root cause or workstream
- severity-weighted priority order
- concrete next action sequence
- explicit residual risks or unknowns
