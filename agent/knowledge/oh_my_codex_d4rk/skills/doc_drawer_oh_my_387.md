/ auto detection.
- Mixed CLI-map teams are supported for both startup and trigger submit behavior.
- Trigger submit differs by CLI:
  - Codex may use queue-first `Tab` on busy panes (strategy-dependent).
  - Claude always uses direct Enter-only (`C-m`) rounds (never queue-first `Tab`).

### Team worker model + thinking resolution (current contract)

Team mode resolves worker **model flags** from one shared launch-arg set (not per-worker model selection).

Model precedence (highest to lowest):
1. Explicit worker model in `OMX_TEAM_WORKER_LAUNCH_ARGS`
2. Inherited leader `--model` flag
3. Low-complexity default from `OMX_DEFAULT_SPARK_MODEL` (legacy alias: `OMX_SPARK_MODEL`) when 1+2 are absent and team `agentType` is low-complexity