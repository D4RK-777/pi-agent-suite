---
name: security-and-auth
description: >-
  Use when implementing or reviewing authentication, authorization, session handling, OAuth,
  permission boundaries, secrets, sensitive-data flows, or security-sensitive backend/frontend
  changes. Triggers on "auth", "login", "OAuth", "JWT", "RBAC", "permissions", "secrets",
  "security review", "vulnerability", or "sensitive data".
trigger: auth, security, permissions
tags:
  - security
  - auth
  - oauth
  - sessions
  - permissions
  - secrets
---

# Security And Auth

## Purpose

Use this skill when a task needs secure identity handling or a risk-focused review. It covers
authentication, authorization, session handling, permission boundaries, secret hygiene, and
abuse-path thinking.

This skill is both an implementation guide and a review lens. It should make security pressure
visible before a change ships.

## When to Use

- Login, signup, session, or token flow changes
- OAuth, SSO, or identity-provider integration
- Role checks, permission boundaries, or route protection
- Secret handling, credential flow, or secure configuration
- Security review of high-risk changes
- Sensitive data access or abuse-path concerns

## Rules

- Separate authentication from authorization; never treat them as the same problem.
- Default to deny when permission logic is unclear.
- Verify object-level ownership, not just broad role membership.
- Never trust client-provided role or ownership claims without server verification.
- Keep secrets out of logs, errors, and client payloads.
- Prefer short-lived credentials and explicit rotation paths.
- Record security-relevant decisions and residual risk when tradeoffs are unavoidable.
- If the primary problem is runtime health, incident management, or operational resilience, hand off to `reliability`.

## Workflow

1. Map the trust boundary.
   - Who is acting, what are they trying to access, and what proves identity?
2. Map the control boundary.
   - What authorization check decides access, and where is it enforced?
3. Review sensitive paths.
   - Tokens, secrets, sessions, resets, role changes, admin paths, external callbacks.
4. Test abuse paths.
   - Missing ownership checks, replay, escalation, token misuse, or secret exposure.
5. State the outcome clearly.
   - Safe, unsafe, or safe with residual risk and required remediation.

## Expected Output

- secure auth or permission implementation guidance
- findings with severity and remediation when reviewing
- explicit notes on trust boundaries, sensitive flows, and residual risk
