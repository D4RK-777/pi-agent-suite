i/__tests__/exec.test.js
node --test dist/hooks/__tests__/codebase-map.test.js
```

Observed status:

- `npm run build` → **PASS**
- `npm run lint` → **PASS**
- `npm test` → **FAIL** (`2590` pass / `2` fail)
- `node --test dist/cli/__tests__/exec.test.js` → **FAIL** (`1` failing test)
- `node --test dist/hooks/__tests__/codebase-map.test.js` → **FAIL** (`1` failing test)

## Exact remaining failing buckets

### 1. `dist/cli/__tests__/exec.test.js`

Failing test:

- `runs codex exec with session-scoped instructions that preserve AGENTS and overlay content`

Observed mismatch:

- expected `instructions-path: .../.omx/state/sessions/omx-*/AGENTS.md`
- actual `instructions-path: .../.omx/team/continue-from-clean-commit-810/worktrees/worker-3/AGENTS.md`

Interpretation: