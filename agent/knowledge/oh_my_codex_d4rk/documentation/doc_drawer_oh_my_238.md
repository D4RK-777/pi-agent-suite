ead the
repo-root `.omx/state/*.json` runtime files for the current workspace.

Compatibility notes:

- `omx tmux-hook` remains a CLI/runtime workflow, not `sdk.omx.tmuxHook.*`
- pass one does not add `sdk.omx.tmuxHook.*`; tmux plugin behavior stays on `sdk.tmux.sendKeys(...)`
- pass one does not add generic `sdk.omx.readJson(...)`, `sdk.omx.list()`, or `sdk.omx.exists()`
- pass one does not add `sdk.pluginState`; keep using `sdk.state`

## Logs

Plugin dispatch and plugin logs are written to:

- `.omx/logs/hooks-YYYY-MM-DD.jsonl`