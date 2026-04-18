ean-commit-810/worktrees/worker-3/AGENTS.md"
```

### 2. `dist/hooks/__tests__/codebase-map.test.js`

Failing test:

- `includes non-src top-level directories`

Observed mismatch:

- the test creates `scripts/notify-hook.js`
- the helper then runs `git add dist/scripts/notify-hook.js`
- `git add` exits with status `128` before the assertion runs

Interpretation:

- This is a **stale test fixture path**.
- The fixture setup and the tracked-path argument do not match, so the test fails before it can validate `generateCodebaseMap()` behavior.

Evidence excerpt:

```text
✖ includes non-src top-level directories
Error: Command failed: git add dist/scripts/notify-hook.js
status: 128
```

## Classification