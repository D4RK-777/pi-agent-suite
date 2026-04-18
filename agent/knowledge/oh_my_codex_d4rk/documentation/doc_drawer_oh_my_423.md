to `0.11.8` across Node and Cargo packages

## Verification evidence

### Targeted regression suite

- `npm run build` ✅
- `node --test --test-reporter=spec dist/hooks/__tests__/notify-hook-auto-nudge.test.js` ✅
- `node --test --test-reporter=spec dist/hooks/__tests__/notify-hook-team-leader-nudge.test.js` ✅
- `node --test --test-reporter=spec dist/hooks/__tests__/notify-fallback-watcher.test.js` ✅

## Remaining risk

- The coverage is targeted at notify-hook and fallback-watcher nudge paths; broader runtime behavior still relies on the full suite and live tmux workflows.
- Future nudge entrypoints should reuse the same deep-interview suppression check to preserve this hotfix contract.