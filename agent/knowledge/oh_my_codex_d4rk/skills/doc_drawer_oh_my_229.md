om prior stages and
return a `StageResult` with status, artifacts, and duration.

## Built-in Stages

- **ralplan**: Consensus planning (planner + architect + critic). Skips only when both `prd-*.md` and `test-spec-*.md` planning artifacts already exist, and carries any `deep-interview-*.md` spec paths forward for traceability.
- **team-exec**: Team execution via Codex CLI workers. Always the OMX execution backend.
- **ralph-verify**: Ralph verification loop with configurable iteration count.

## State Management

Pipeline state persists via the ModeState system at `.omx/state/pipeline-state.json`.
The HUD renders pipeline phase automatically. Resume is supported from the last incomplete stage.