ardening for watcher shutdown cleanup and `check:no-unused` cleanup in setup

## Validation evidence

| Check | Command | Result |
|---|---|---|
| Build | `npm run build` | PASS |
| Full test suite | `npm test` | PASS (`1940` pass / `0` fail, `duration_ms 206426.374278`) |
| No-unused type gate | `npm run check:no-unused` | PASS |
| CLI help smoke | `node bin/omx.js --help` | PASS |
| Version smoke | `node bin/omx.js version` | PASS (`oh-my-codex v0.8.4`) |
| Doctor smoke | `node bin/omx.js doctor` | PASS (`9 passed, 0 warnings, 0 failed`) |
| Setup dry-run smoke | `node bin/omx.js setup --dry-run` | PASS |
| Targeted watcher regression | `node --test dist/hooks/__tests__/notify-fallback-watcher.test.js` | PASS (`6` pass / `0` fail) |

## Risk notes