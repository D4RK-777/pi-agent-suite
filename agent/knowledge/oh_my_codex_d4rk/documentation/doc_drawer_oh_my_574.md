# Rust Runtime Thin-Adapter Contract

## Canonical ownership

Rust core is the single semantic owner for:

- authority
- lifecycle/session state
- dispatch/backlog
- mailbox delivery state
- replay/recovery
- readiness/diagnostics
- canonical mux operations

JS, HUD, CLI, and tmux are thin delivery/observer adapters. They may read
compatibility artifacts, but they MUST NOT define or mutate semantic truth on
their own.

Current migration follow-ups that still fall short of this target are tracked in
`docs/qa/runtime-team-seam-audit-2026-04-01.md`.

## Compatibility artifacts

Legacy readers continue to read the same state files, but only as
Rust-authored compatibility views.