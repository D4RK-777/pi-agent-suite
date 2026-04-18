---
name: frontend-engineering
description: >-
  Use when building or changing frontend implementation: components, pages, layouts, client-side
  state, forms, styling, responsive behavior, or data-fetching patterns in React or Next.js.
  Triggers on "component", "page", "layout", "frontend", "React", "Next.js", "hook", "form",
  "state", "responsive", or when a task touches browser-side code.
trigger: frontend, component, React, Next.js
tags:
  - frontend
  - react
  - nextjs
  - typescript
  - components
  - styling
  - state
  - responsive
---

# Frontend Engineering

## Purpose

Use this skill for frontend implementation and UI architecture. It covers component boundaries,
state ownership, rendering strategy, styling approach, interaction design, and browser-facing
data flow.

This skill is for building frontend behavior correctly. Pair it with `gsap` for motion-heavy
work, `frontend-quality` for readiness and audit pressure, and `google-stitch` when the design
direction still needs to be shaped before implementation.

## When to Use

- Building or changing components, pages, layouts, or screens
- Refactoring frontend structure or component boundaries
- Choosing between server and client rendering patterns
- Designing state ownership, forms, or interaction flows
- Implementing styling systems, theming, or responsive behavior
- Wiring data-fetching or mutation flows into UI surfaces

## Rules

- Define component boundaries before writing implementation.
- Keep state as local as practical; lift it only when shared ownership is real.
- Prefer explicit props and data flow over hidden coupling.
- Choose rendering mode deliberately: server when possible, client when necessary.
- Use CSS Modules for component styling. Use design tokens (CSS custom properties) for colors, spacing, and typography. Do NOT use Tailwind unless the project explicitly requires it.
- Keep forms, loading states, empty states, and failure states first-class.
- Avoid fragile styling shortcuts that break responsive behavior or accessibility.
- If motion is central to the experience, load `gsap`.
- If readiness, accessibility, performance, or polish is the main concern, load `frontend-quality`.

## Workflow

1. Define the surface.
   - What is being built: a component, page, layout, flow, or refactor?
2. Define the structure.
   - Component boundaries, state ownership, rendering mode, and styling approach.
3. Implement the behavior.
   - Build the happy path, loading path, empty path, and failure path.
4. Check the browser realities.
   - Responsive behavior, keyboard flow, semantics, focus, and error handling.
5. Pressure-test the result.
   - Verify the implementation still fits the existing architecture and quality bar.

## Expected Output

- production-ready frontend implementation
- clear component and state boundaries
- responsive, typed, and maintainable UI code
- explicit notes where motion, accessibility, or performance follow-up matters
