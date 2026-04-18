---
name: incident-and-recovery
description: >-
  Use when handling active breakage, incident framing, rollback planning, recovery sequencing, or
  stabilizing a flaky system. Triggers on "incident", "outage", "rollback", "recovery", "broken
  in production", "staging is down", "blast radius", or "how do we stabilize this?".
trigger: incident, outage, recovery
tags:
  - reliability
  - incident
  - recovery
  - rollback
  - stabilization
  - operations
---

# Incident And Recovery

## Purpose

Use this skill when a system is actively failing or unstable and the job is to stabilize,
understand blast radius, recover safely, and avoid making things worse under pressure.

This skill is about operational response quality: containment, rollback thinking, recovery
sequencing, and clear next steps.

## When to Use

- Production or staging is broken
- A release needs rollback or containment thinking
- A flaky system needs stabilization before optimization
- Incident response steps are unclear or too improvised
- A failure needs explicit blast-radius and recovery framing

## Rules

- Stabilize first, optimize later.
- Prefer containment and rollback over clever fixes under pressure.
- Preserve evidence before destructive cleanup when possible.
- State blast radius explicitly: who is affected, what is failing, what is still safe.
- Do not declare recovery until verification proves the system is healthy.
- Hand off deeper root-cause analysis to `debugger` or implementation changes to the owning lead agent once the incident is stable.

## Workflow

1. Frame the incident.
   - What broke, when, for whom, and how badly?
2. Contain the damage.
   - Freeze rollout, disable the bad path, fail closed, or rollback.
3. Choose the safest recovery path.
   - Restore service first, then investigate.
4. Verify recovery.
   - Smoke check the affected paths and key dependencies.
5. Record the next move.
   - Root-cause work, missing safeguards, and follow-up hardening.

## Expected Output

- incident framing with blast radius
- safest immediate recovery path
- rollback or stabilization guidance
- explicit verification and follow-up steps
