---
name: frontend-quality
description: >-
  Use when auditing or improving frontend readiness: accessibility, performance, responsive
  behavior, design-token discipline, interaction polish, or production confidence. Triggers on
  "a11y", "accessibility", "performance", "Core Web Vitals", "responsive", "quality pass",
  "polish", or "is this ready to ship?".
trigger: frontend quality, accessibility, performance
tags:
  - frontend
  - accessibility
  - performance
  - responsive
  - design-tokens
  - quality
  - wcag
---

# Frontend Quality

## Purpose

Use this skill as the production-readiness and audit layer for frontend work. It covers
accessibility, responsiveness, performance, UI consistency, and the small failure modes that
make interfaces feel broken even when they technically render.

This skill should raise the bar before release. It is not a replacement for implementation;
it is the pressure pass that makes implementation safe to ship.

## When to Use

- A frontend change needs a readiness pass
- Accessibility or inclusive interaction quality matters
- Performance, rendering cost, or bundle behavior is a concern
- Responsive layouts feel brittle across breakpoints
- A UI looks done but still feels inconsistent or untrustworthy
- The team needs a ship/no-ship view on a frontend surface

## Rules

- Accessibility is a baseline, not an optional refinement.
- Check keyboard flow, focus visibility, semantics, labels, and error messaging.
- Verify the interface at real breakpoints, not just one happy-path viewport.
- Use existing tokens and theme rules instead of ad hoc visual values.
- Treat loading, empty, disabled, and failure states as part of quality.
- Look for jank, layout shift, slow paths, oversized bundles, and unnecessary client work.
- State residual risk clearly when time prevents a full pass.
- If the main issue is implementation structure, load `frontend-engineering`.

## Workflow

1. Identify the risk surface.
   - Accessibility, responsiveness, performance, consistency, or all of them.
2. Audit the critical paths.
   - Primary flows, interactive controls, forms, navigation, and state transitions.
3. Check non-happy states.
   - Loading, empty, disabled, validation, and error paths.
4. Assess ship confidence.
   - What is solid, what is weak, and what would likely break first?
5. Report fixes in priority order.
   - Start with blocking issues, then visible degradation, then polish.

## Expected Output

- readiness findings in practical priority order
- accessibility and responsive gaps with concrete fixes
- performance or token-discipline issues when present
- explicit residual risk and ship confidence
