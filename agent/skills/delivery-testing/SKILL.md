---
name: delivery-testing
description: >-
  Use when planning, writing, or reviewing tests and verification paths for new behavior,
  regressions, smoke checks, or release confidence. Triggers on "test", "coverage", "verify",
  "smoke test", "QA", "release confidence", or when a change needs proof that it works.
trigger: test, verify, coverage
tags:
  - testing
  - verification
  - coverage
  - qa
  - release-confidence
---

# Delivery Testing

## Purpose

Use this skill for verification strategy. It covers what to test, where to test it, and how to
decide whether confidence is high enough to ship.

The goal is not more tests by default. The goal is the right tests at the right level, plus a
clear statement of what remains unverified.

## When to Use

- A change needs a test plan
- Tests need to be written or expanded
- Release confidence depends on smoke coverage or regression checks
- A bug fix needs verification against the actual failure mode
- Coverage exists but the important paths are still unclear

## Rules

- Test behavior, not implementation trivia.
- Prefer the cheapest test level that can prove the requirement.
- Cover the happy path, failure path, and the most likely regression path.
- Add smoke coverage for critical user or system flows.
- State clearly what is not tested when full coverage is not practical.
- If the system is actively unstable, coordinate with `debugger` or `reliability` before inventing more tests.

## Workflow

1. Identify the risk.
   - What can break, and who would notice first?
2. Choose the test layer.
   - Unit, integration, component, end-to-end, smoke, or manual verification.
3. Define the minimum credible set.
   - The few tests that would meaningfully increase confidence.
4. Verify against the real failure mode.
   - Especially for regressions and bug fixes.
5. Report confidence honestly.
   - Good enough to ship, or still missing coverage in critical paths.

## Expected Output

- targeted verification plan
- test coverage recommendations
- explicit confidence level and remaining gaps
