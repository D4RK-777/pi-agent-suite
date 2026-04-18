---
name: gsap
description: >-
  Use when building or refining motion with GSAP in frontend code: timelines, ScrollTrigger,
  scroll-linked scenes, hero motion, section reveals, pinned storytelling, or interaction
  choreography. Triggers on "GSAP", "ScrollTrigger", "timeline", "scroll animation", "pinned
  section", "motion", or when the user wants intentional premium frontend animation.
trigger: gsap, ScrollTrigger, timeline, motion
tags:
  - frontend
  - animation
  - gsap
  - scrolltrigger
  - motion
  - react
  - nextjs
---

# GSAP

## Purpose

Use this skill when the main challenge is motion design and implementation with GSAP. It covers
timeline composition, ScrollTrigger setup, sequencing, performance discipline, and how to keep
animation expressive without making the UI brittle.

This skill is for motion-heavy frontend work. Pair it with `frontend-engineering` for component
structure and rendering decisions, and with `frontend-quality` for accessibility, reduced-motion,
responsiveness, and production-readiness review.

## When to Use

- Scroll-based storytelling sections or pinned scenes
- Hero motion, reveals, transitions, and interaction choreography
- Complex sequencing where CSS transitions are too limited
- Animation systems that need timeline coordination
- Motion refactors where the result should feel intentional instead of decorative

## Rules

- Start with the narrative purpose of the motion before writing animation code.
- Prefer a few strong timelines over many disconnected one-off tweens.
- Scope selectors safely and clean up all GSAP instances on unmount.
- Respect reduced-motion and avoid making content unusable without animation.
- Keep animation state separate from core business logic.
- Use ScrollTrigger intentionally; do not pin or scrub by default.
- Favor smoothness, clarity, and restraint over constant movement.
- If the issue is mostly layout, structure, or data flow, load `frontend-engineering` first.
- If the issue is mostly readiness, accessibility, or performance, load `frontend-quality`.

## Workflow

1. Define the motion job.
   - Is this reveal, transition, storytelling, emphasis, or feedback?
2. Define the scene boundaries.
   - What elements participate, what triggers the motion, and when should it end?
3. Build the timeline.
   - Sequence the main beats with clear start and end states.
4. Handle lifecycle and fallbacks.
   - Scope selectors, clean up triggers, and support reduced-motion.
5. Pressure-test the feel.
   - Check performance, responsiveness, readability, and whether the motion improves the experience.

## Expected Output

- motion plans with clear animation intent
- maintainable GSAP implementation patterns
- ScrollTrigger usage that is deliberate rather than noisy
- explicit notes on reduced-motion, cleanup, and performance follow-up
