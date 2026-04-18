tories
Error: Command failed: git add dist/scripts/notify-hook.js
status: 128
```

## Classification

These two failures are the only remaining buckets seen in the fresh local suite run recorded for this task:

1. **worker-context contract drift** in `exec.test`
2. **stale fixture path drift** in `codebase-map.test`

No additional failure buckets were observed in the same `npm test` run.

## Changed files

- `docs/qa/remaining-suite-drift-2026-03-19.md` — captured the remaining failure buckets, reproduction commands, and verification evidence from the clean-commit rerun.

## Notes