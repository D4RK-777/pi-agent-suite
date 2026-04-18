MO.md` pass (or are documented if environment-limited)

### Smoke verification evidence (2026-03-02)

| Command | Exit | Evidence |
|---|---:|---|
| `npm run build` | 0 | build completed |
| `npm test` | 0 | test pipeline completed |
| `npm run check:no-unused` | 0 | `tsc -p tsconfig.no-unused.json` succeeded |
| `node bin/omx.js --help` | 0 | CLI usage rendered |
| `node bin/omx.js doctor` | 0 | `Results: 9 passed, 0 warnings, 0 failed` |
| `node bin/omx.js version` | 0 | `oh-my-codex v0.7.6` |
| `node bin/omx.js status` | 0 | mode status rendered |
| `node bin/omx.js setup --dry-run` | 0 | dry-run setup completed |
| `node bin/omx.js cancel` | 0 | cancel command completed |