antics instead of the earlier v1 scaffold.

## Verified evidence

### Build
- `npm run build` → PASS

### Focused tests
- `node --test dist/autoresearch/__tests__/runtime.test.js dist/cli/__tests__/autoresearch.test.js dist/cli/__tests__/index.test.js dist/cli/__tests__/nested-help-routing.test.js dist/team/__tests__/worktree.test.js dist/modes/__tests__/base-autoresearch-contract.test.js` → PASS
- `node --test dist/cli/__tests__/session-search-help.test.js` → PASS