---
name: delivery-code-review
description: >-
  Use when performing a findings-first review of a code change, pull request, or implementation
  plan. Triggers on "review this", "code review", "what did we miss?", "merge-ready", "risk
  pass", or when a change needs an independent quality gate before shipping.
trigger: review, code review, merge-ready
tags:
  - review
  - quality
  - regressions
  - risk
  - merge-readiness
  - testing
---

# Delivery Code Review

## Purpose

Use this skill for structured code review with emphasis on risk, regressions, weak assumptions,
missing tests, and merge readiness.

This skill should behave like an independent quality gate. The goal is not to praise the change
or rewrite it blindly; the goal is to surface what can break, what is under-proven, and what
must be fixed or verified before confidence is justified.

## When to Use

- Reviewing a pull request or implementation diff
- Pressure-testing a change before merge or release
- Looking for regressions, risky assumptions, or hidden breakage
- Checking whether test coverage matches the actual risk
- Producing a findings-first review for another agent or teammate

## Rules

- Findings come first, ordered by severity.
- Focus on correctness, regressions, safety, and missing proof before style nits.
- Review behavior, not just code shape.
- Treat missing tests as a real risk when behavior changed materially.
- Say explicitly when evidence is insufficient rather than assuming safety.
- Keep summaries short and only after the findings.
- If the code appears safe, say that clearly and note any remaining blind spots.
- If the task is primarily test planning, load `delivery-testing`.

## Workflow

1. Identify the change surface.
   - What behavior changed, and what users or systems depend on it?
2. Look for breakage risk.
   - Regressions, edge cases, failure paths, compatibility issues, and unsafe assumptions.
3. Check proof.
   - Tests, validation steps, runtime safeguards, and rollback confidence.
4. Write findings first.
   - Severity, location, why it matters, and what needs to change.
5. State residual risk.
   - What still looks uncertain even if no blocking bug is proven?

## Expected Output

- severity-ordered review findings
- open questions or assumptions where evidence is weak
- explicit residual risk and confidence level
- short summary only after the findings
