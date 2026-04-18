# Agent Tiers

This file defines practical tier guidance for OMX agent routing.

## Mental Model

OMX now separates three concepts:

- `role`: what the agent is responsible for (`executor`, `planner`, `architect`)
- `tier`: how much reasoning/cost to spend (`LOW`, `STANDARD`, `THOROUGH`)
- `posture`: how the role behaves (`frontier-orchestrator`, `deep-worker`, `fast-lane`)

Use role to choose responsibility, tier to choose depth, and posture to choose operating style.

## Tiers

- `LOW`:
  Fast lookups and narrow checks.
  Use for simple exploration, style checks, and lightweight doc edits.
  Typical roles: `explore`, `style-reviewer`, `writer`.