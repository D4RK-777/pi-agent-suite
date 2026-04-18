esearchLoop()` relaunches Codex after `processAutoresearchCandidate()` unless the run aborts/errors.

### 2. Repo-root state authority
**Pass.**
- repo-root active-run lock lives at `.omx/state/autoresearch-state.json`.
- per-run manifest, candidate, ledger, and latest evaluator files live under `.omx/logs/autoresearch/<run-id>/`.
- worktree-local runtime artifacts are limited to `results.tsv` and allowlisted logs.

### 3. Fresh-run semantics
**Pass.**
- fresh launches compute a run tag and plan `autoresearch/<mission-slug>/<run-tag>` plus `autoresearch-<mission-slug>-<run-tag>`.
- focused worktree coverage now asserts run-tagged branch/path naming.