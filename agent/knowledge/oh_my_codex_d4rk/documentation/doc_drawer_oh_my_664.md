et localization
- version bump and release metadata updates required for `0.9.1`

## Validation plan

| Check | Command | Status |
|---|---|---|
| Version sync | `node scripts/check-version-sync.mjs --tag v0.9.1` | PASS |
| Lint | `npm run lint` | PASS |
| TypeScript noEmit | `npx tsc --noEmit` | PASS |
| No-unused gate | `npm run check:no-unused` | PASS |
| Full test suite | `npm test` | PASS (`2397` pass / `0` fail) |
| Smoke test coverage | `node --test scripts/__tests__/smoke-packed-install.test.mjs` | PASS (`1` pass / `0` fail) |
| Release build | `npm run build:full` | PASS |
| Packed install smoke | `npm run smoke:packed-install` | PASS |
| Packed tarball dry run | `npm pack --dry-run` | PASS (`oh-my-codex-0.9.1.tgz`) |

## Historical release note