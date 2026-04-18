ty, stop for operator intervention; if clean, log interrupted/noop style outcome

## Decision policy

- Baseline row is always recorded.
- `pass=false` => discard.
- evaluator error/crash => discard.
- `keep_policy=score_improvement` => keep only when `pass=true` and score improves over last kept score; pass without comparable score is `ambiguous` and discarded.
- `keep_policy=pass_only` => any `pass=true` candidate is kept.
- Discard / ambiguous / error paths must reset to the last kept commit.

## Resume

`--resume <run-id>` must fail with actionable errors when:
- manifest is missing
- referenced worktree is missing
- worktree is dirty outside allowlisted runtime artifacts
- manifest is terminal

Successful resume continues from the last kept commit and existing results history.