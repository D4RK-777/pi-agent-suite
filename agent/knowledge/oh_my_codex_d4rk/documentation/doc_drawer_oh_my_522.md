esearch-<mission-slug>-<run-tag>`
- repo-root run artifacts under `.omx/logs/autoresearch/<run-id>/`

Repo-root state responsibilities:
- `.omx/state/autoresearch-state.json` = active-run pointer/lock only
- `.omx/logs/autoresearch/<run-id>/manifest.json` = authoritative per-run state
- `.omx/logs/autoresearch/<run-id>/candidate.json` = candidate handoff from the just-finished Codex session
- `.omx/logs/autoresearch/<run-id>/iteration-ledger.json` = durable iteration history
- `.omx/logs/autoresearch/<run-id>/latest-evaluator-result.json` = latest evaluator output

Worktree-local state responsibilities:
- `results.tsv`
- optional evaluator logs such as `run.log`
- these runtime-generated files must be excluded via worktree-local `.git/info/exclude`

## Candidate artifact