# Project Context Capture

## Purpose

Capture repo-specific operating context without polluting the shared D4rkMynd core.

## Use When

- onboarding a project with brand or product constraints
- migrating a large `CLAUDE.md`, `AGENTS.md`, or repo guide into cleaner structure
- deciding whether guidance belongs in shared core or in one repo

## Steps

1. Extract the project-specific facts: brand rules, immutable copy, product names, file paths, delivery schedules, and risk hotspots.
2. Separate reusable operating logic from repo-local context.
3. Move reusable logic into shared standards, cookbooks, skills, or agent files.
4. Keep repo-local context inside the project repo in a durable file such as `CLAUDE.md`, `AGENTS.md`, or `docs/project-context.md`.
5. Add a short note or link in shared docs only when cross-reference is genuinely useful.

## Output

- clean split between shared and project-local guidance
- repo-local context file location
- migration note for anything promoted into shared core
