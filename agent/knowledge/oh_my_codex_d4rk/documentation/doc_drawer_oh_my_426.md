1.9` across Node and Cargo packages

## Verification evidence

### Targeted release regression suite

- `npm run build` ✅
- `npm run lint` ✅
- `npm run check:no-unused` ✅
- `node --test --test-reporter=spec dist/cli/__tests__/version-sync-contract.test.js` ✅
- `node --test --test-reporter=spec dist/cli/__tests__/setup-refresh.test.js dist/cli/__tests__/setup-scope.test.js dist/cli/__tests__/doctor-warning-copy.test.js` ✅
- `node --test --test-reporter=spec dist/hooks/__tests__/explore-routing.test.js dist/hooks/__tests__/explore-sparkshell-guidance-contract.test.js dist/hooks/__tests__/deep-interview-contract.test.js dist/hooks/__tests__/notify-fallback-watcher.test.js dist/hooks/__tests__/notify-hook-auto-nudge.test.js dist/hooks/__tests__/agents-overlay.test.js` ✅