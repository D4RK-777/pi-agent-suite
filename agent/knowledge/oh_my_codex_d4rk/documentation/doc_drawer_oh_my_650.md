fy-fallback-watcher.test.ts` to stabilize full-suite verification under load

## Validation evidence

| Check | Command | Result |
|---|---|---|
| Build | `npm run build` | PASS (`real 9.15`) |
| Full test suite | `npm test` | PASS (`1926` pass / `0` fail, `real 498.76`, after clean `dist/` rebuild) |
| No-unused type gate | `npm run check:no-unused` | PASS (`real 4.73`) |
| CLI help smoke | `node bin/omx.js --help` | PASS (`real 0.10`) |
| Version smoke | `node bin/omx.js version` | PASS (`oh-my-codex v0.8.3`, `real 0.10`) |
| Status smoke | `node bin/omx.js status` | PASS (`ultrawork: ACTIVE (phase: debugging-verification)`, `real 0.13`) |
| Doctor smoke | `node bin/omx.js doctor` | PASS (`9 passed, 0 warnings, 0 failed`, `real 0.21`) |