dbox contract

`<mission-dir>` must be inside a git repo and contain `mission.md` plus `sandbox.md`.

`sandbox.md` YAML frontmatter must define:
- `evaluator.command`
- `evaluator.format: json`
- optional `evaluator.keep_policy: score_improvement | pass_only`

Evaluator stdout must be JSON with required boolean `pass` and optional numeric `score`.

## Runtime model

Fresh launch creates:
- branch `autoresearch/<mission-slug>/<run-tag>`
- worktree `<repo>.omx-worktrees/autoresearch-<mission-slug>-<run-tag>`
- repo-root run artifacts under `.omx/logs/autoresearch/<run-id>/`