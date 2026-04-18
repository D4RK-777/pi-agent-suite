`init --flags`, `--resume`)
**Pass on current branch.**
Existing expert/runtime flows remain intact.

### 8. Bare `omx autoresearch init` documented as novice alias
**Fail on current branch.**
Bare `init` is routed into guided mode, but help/docs do not explain the compatibility semantics required by the PRD.

### 9. Non-interactive no-arg failure preserved
**Pass on current branch.**
The TTY guard still rejects no-arg non-interactive invocation.

### 10. Regression coverage for interview/draft/confirm path
**Fail on current branch.**
Those tests are not present yet.

## Documentation follow-ups once implementation lands