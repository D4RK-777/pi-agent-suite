atus` | PASS |
| Doctor smoke | `node bin/omx.js doctor` | PASS (`9 passed, 0 warnings, 0 failed`) |
| Setup dry-run smoke | `node bin/omx.js setup --dry-run` | PASS |
| Cancel smoke | `node bin/omx.js cancel` | PASS |

## Risk notes

- No failing checks observed in release validation.
- `npm test` runtime was long (~721s) due expected long-running notification/tmux integration tests; all completed successfully.

## Final verdict

Release **0.8.1** is **ready to publish** based on current local verification evidence.