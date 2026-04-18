rkflow validation
- release-note and QA draft creation for `0.9.0`

## Validation evidence completed

| Check | Command | Result |
|---|---|---|
| Full source build | `npm run build:full` | PASS |
| CLI help smoke | `node bin/omx.js --help` | PASS |
| Version smoke | `node bin/omx.js version` | PASS (`oh-my-codex v0.9.0`) |
| Version sync | `node scripts/check-version-sync.mjs --tag v0.9.0` | PASS |
| Ask help smoke | `node bin/omx.js ask --help` | PASS |
| HUD help smoke | `node bin/omx.js hud --help` | PASS |
| Doctor smoke | `node bin/omx.js doctor` | PASS (`10 passed, 0 warnings, 0 failed`) |
| Status smoke | `node bin/omx.js status` | PASS |
| Setup dry-run smoke | `node bin/omx.js setup --dry-run` | PASS |
| Explore help smoke | `node bin/omx.js explore --help` | PASS |