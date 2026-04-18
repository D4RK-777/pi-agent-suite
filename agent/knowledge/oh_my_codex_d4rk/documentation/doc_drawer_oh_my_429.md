mode for worker isolation` (#416)
- `feat(team): add per-worker role routing and task decomposition`

### Changed
- `docs: OpenClaw integration guide for notifications` (#413)
- `ci: add CI Status gate job for branch protection` (#423)
- `refactor(mcp): extract omx_run_team_* to dedicated team-server.ts` (#431)
- `docs(changelog): update unreleased notes for main...dev`

### Fixed
- OpenClaw native gateway notification path.
- Tmux startup/injection/session-targeting regressions.
- Team cleanup, scale-up layout preservation, and shutdown/resume regressions.
- Ralph CLI task parsing option-value leakage.
- Skills canonical OMX path normalization.