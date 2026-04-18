|
| Doctor smoke | `node bin/omx.js doctor` | PASS (`9 passed, 0 warnings, 0 failed`, `real 0.21`) |
| Setup dry-run smoke | `node bin/omx.js setup --dry-run` | PASS (`real 0.58`) |
| Cancel smoke | `node bin/omx.js cancel` | PASS (`Cancelled: ultrawork`) |
| Gemini worker targeted tests | `node --test dist/team/__tests__/tmux-session.test.js --test-name-pattern='gemini|buildWorkerProcessLaunchSpec returns command/args/env for prompt process spawn'` | PASS (`127` pass / `0` fail, `real 1.80`) |
| Gemini runtime targeted tests | `node --test dist/team/__tests__/runtime.test.js --test-name-pattern='startTeam launches gemini workers with startup prompt and no default model passthrough'` | PASS (`54` pass / `0` fail, `real 66.40`) |