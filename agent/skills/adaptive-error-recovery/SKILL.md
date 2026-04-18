---
name: adaptive-error-recovery
description: >-
  Use this skill when errors persist after repeated attempts, when a task is stuck for several
  minutes, when the user says "try again" without a strategy change, or when the same failure
  pattern appears three or more times. It enforces a 3-strikes-and-pivot workflow so the agent
  stops repeating the same approach and switches to a meaningfully different recovery path.
trigger: error recovery, try again, still broken, same error, stuck, repeated failure
tags:
  - recovery
  - debugging
  - resilience
  - triage
version: 1.0.0
---

# Adaptive Error Recovery - 3 Strikes & PIVOT

## Purpose

Use this skill when recovery work is looping, repeated retries are not changing the outcome, or a
stuck task needs a deliberate strategy shift instead of more of the same.

## When to Use

- The same error pattern appears 3 or more times with the same strategy
- The user says "try again", "still broken", or "still not working" without a strategy change
- A task has been stuck for several minutes with no measurable progress
- You catch yourself about to say "let me try again" without changing approach
- Repeated tool calls or edits are producing the same failure
- You need to decide whether to pivot, escalate, or call a specialist

## Rules

- Count strikes by strategy, not by individual tool call.
- When ONE approach fails 3 times with the SAME error pattern, STOP and PIVOT immediately.
- A pivot must be a COMPLETELY DIFFERENT angle — not a minor variation.
- Never retry the exact same fix after 3 failures.
- Never say "let me try again" without documenting what changed.
- When no strategy is producing progress, escalate with a structured problem statement.
- Always document the attempt log, pivot decision, and new approach when switching strategies.
- If the user says "still not working", treat it as a mandatory pivot signal.

## Core Rule: 3 STRIKES = MANDATORY PIVOT

When ONE approach fails 3 times with the SAME error pattern, you MUST:
1. STOP using that strategy immediately
2. Document WHY it failed
3. PIVOT to a COMPLETELY DIFFERENT strategy
4. Never retry the same approach without fundamental change

## Strike Counter System

**Track attempts per STRATEGY, not per tool call.**

| Strike | What It Means |
|--------|---------------|
| Strike 1 | First attempt failed - note error pattern |
| Strike 2 | Second attempt failed - same pattern = concerning |
| Strike 3 | Third failure with same pattern = **PIVOT NOW** |

**A "strike" = same strategy + same/similar error. NOT every tool call.**

## Workflow

1. Count strikes by strategy, not by individual tool call.
2. Stop once the same strategy hits the same failure pattern three times.
3. Record why the current strategy failed.
4. Pivot to a meaningfully different strategy.
5. Escalate cleanly if no strategy is producing progress.

## The 5 Strategies (Use in Order, Pivot When Stuck)

### 1. DIRECT Approach
Read the file, understand the code, apply fix directly.
- **When**: First try, obvious bugs, type errors
- **Strike condition**: Same TypeScript error, same logic bug

### 2. RESEARCH Approach
Search docs, web, codebase patterns, understand before fixing.
- **When**: Direct failed 2-3x, unfamiliar API, unclear error
- **Strike condition**: Same misunderstanding persists

### 3. AGENT Approach
Spawn a specialist subagent for fresh perspective.
- **When**: Research failed, need different expertise
- **Strike condition**: Agent suggests same fix you already tried

### 4. SIMPLIFY Approach
Strip to minimum viable case, isolate the problem.
- **When**: Everything else failed, problem is complex
- **Strike condition**: Can't reproduce in simple case

### 5. ESCALATE Approach
State clearly what you tried, what the error is, what you need.
- **When**: Nothing else worked, need user input
- **Output format**: Structured problem statement

## Pivot Triggers (MUST Act on These)

- ❌ Same error after 3 attempts → **PIVOT MANDATORY**
- ❌ No measurable progress after 3 attempts → **PIVOT MANDATORY**
- ❌ "Let me try again" without strategy change → **DENIED**
- ❌ User says "still not working" → **PIVOT MANDATORY**
- ❌ Stuck for >5 minutes → **PIVOT MANDATORY**

## Required Output Format

When pivoting, ALWAYS document in this format:

```markdown
## Attempt Log
| # | Strategy | Result | Error Pattern |
|---|----------|--------|---------------|
| 1 | Direct   | ❌     | TypeScript TS2322 |
| 2 | Direct   | ❌     | Same TS2322, diff line |
| 3 | Direct   | ❌     | Third TS2322 → PIVOT |

## Pivot Decision
**From:** Direct (3 strikes - same error pattern)
**To:** Research approach
**Reason:** "Tried direct fixes 3x, TypeScript error persists. Need to understand type system issue before fixing."

## New Attempt
[Describe COMPLETELY different approach - new strategy, new angle]
```

## What PIVOT Means

**PIVOT = COMPLETELY DIFFERENT ANGLE, not minor variation**

Bad pivot (rejected):
- "Let me try editing a different line"
- "Maybe I should use a different tool call"
- "Let me attempt the same fix again"

Good pivot:
- Direct failed → Research: understand root cause before touching code
- Research failed → Agent: get fresh perspective from specialist
- Agent failed → Simplify: isolate to minimum reproducible case
- All failed → Escalate: clearly state what you need from user

## Anti-Loop Rules

1. **Never say "let me try again"** without documenting what changed
2. **Never retry the exact same fix** after 3 failures
3. **Never keep the same strategy** when hitting the same error
4. **Never ignore "still not working"** - it's a pivot signal

## Quick Reference

```
STRIKE 1 → Note error, continue same strategy
STRIKE 2 → Growing concern, consider backup approach
STRIKE 3 → STOP. PIVOT NOW. Never retry same approach.
```
