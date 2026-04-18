urrent branch.**
Guided setup returns launch-ready mission data and tmux launch happens immediately.

### 5. Placeholder evaluator rejection before launch
**Fail on current branch.**
There is no blocked-pattern gate for placeholder evaluator commands.

### 6. Top-level seeded novice flags (`--topic`, `--evaluator`, `--keep-policy`, `--slug`)
**Fail on current branch.**
Those flags are not accepted at top level; only `init` parses them today.

### 7. Expert flows preserved (`<mission-dir>`, `init --flags`, `--resume`)
**Pass on current branch.**
Existing expert/runtime flows remain intact.