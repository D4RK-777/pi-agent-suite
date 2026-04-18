ch-<mission-slug>-<run-tag>`.
- focused worktree coverage now asserts run-tagged branch/path naming.

### 4. Resume contract
**Pass.**
- CLI parses `--resume <run-id>`.
- runtime rejects missing manifest, missing worktree, dirty worktree, and terminal runs.

### 5. Keep/discard/reset decision policy
**Pass.**
- baseline row is seeded.
- evaluator failure/error discards.
- `pass_only` keeps any pass.
- `score_improvement` requires comparable numeric scores and improvement; otherwise ambiguous/discard.
- discard paths reset to `last_kept_commit`.