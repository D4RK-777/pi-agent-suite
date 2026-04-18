# Release Notes - 0.7.6

Status: Prepared on **2026-03-02**.

Current package version: **0.7.6**.

## Scope policy

This release note is based strictly on:

- `git log --no-merges main..dev`
- `git diff --shortstat main...dev`

## Sections

### Highlights
- Team reliability hardening across tmux/session targeting, cleanup flows, and role-based decomposition.
- MCP team runtime extraction and improved CI gate visibility.
- OpenClaw and notify-hook reliability/documentation updates.

### Added
- `feat(team): add dedicated ralph auto-run cleanup policy` (#407, #412)
- `feat(team): add dedicated tmux session mode for worker isolation` (#416)
- `feat(team): add per-worker role routing and task decomposition`