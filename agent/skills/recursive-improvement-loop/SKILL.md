---
name: recursive-improvement-loop
description: >-
  Use when the system discovers a recurring failure, repeated user correction, stale skill,
  project-local leak into shared core, or a pattern that should be captured and improved instead
  of rediscovered. Triggers on \"we keep hitting this\", \"don't repeat this\", \"improve the
  agent\", \"make this part of the system\", or when reports and feedback should feed back into
  better skills, overlays, docs, or processes.
trigger: improvement, learning loop, drift correction, feedback capture
tags:
  - improvement
  - learning
  - feedback
  - drift
  - maintenance
  - governance
---

# Recursive Improvement Loop

## Purpose

Use this skill to convert discovered weaknesses into durable system improvements.

This skill is not about solving the immediate task alone. It is about making sure the same class
of mistake becomes less likely next time by updating the right layer: skill, overlay, agent doc,
process, test expectation, or memory note.

## When to Use

- A user correction reveals a repeated weakness
- The same issue appears across multiple tasks or repos
- A report or audit exposes a missing capability
- Shared core contains project-specific leakage
- A project overlay keeps compensating for the same missing core behavior
- A failure should become a standing rule, skill improvement, or local memory note

## Rules

- Fix the right layer, not just the nearest file.
- Distinguish shared-core improvements from project-local overlays.
- Prefer a small number of durable changes over a giant reactive patch set.
- Record the trigger that caused the improvement so the change has context.
- If the issue is still uncertain, capture it as a tracked hypothesis instead of pretending it is solved.
- Close the loop with an explicit recommendation: skill update, overlay update, process update, test gap, or no action.

## Workflow

1. Capture the signal.
   - What happened, who noticed it, and what pattern does it reveal?
2. Classify the layer.
   - Shared core, project overlay, agent definition, process, cookbook, or memory note?
3. Choose the smallest durable fix.
   - Improve an existing skill, add a missing one, update a cookbook, or record repo-local guidance.
4. Prevent drift.
   - Update manifests, cross-references, or migration notes where needed.
5. Make the next recurrence cheaper.
   - State how the new rule or artifact should change future behavior.

## Expected Output

- improvement trigger summary
- correct target layer for the fix
- recommended durable change
- note on what remains project-local versus shared
- follow-up action to close the loop
