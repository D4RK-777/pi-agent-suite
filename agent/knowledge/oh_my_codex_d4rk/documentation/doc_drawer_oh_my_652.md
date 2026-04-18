with startup prompt and no default model passthrough'` | PASS (`54` pass / `0` fail, `real 66.40`) |
| Gemini tmux demo targeted tests | `node --test dist/team/__tests__/tmux-claude-workers-demo.test.js --test-name-pattern='gemini'` | PASS (`18` pass / `0` fail, `real 0.38`) |

## Risk notes

- This is a focused patch release centered on the Gemini worker startup hotfix after the `0.8.2` dev release line.
- Primary regression surface is the team runtime / tmux-session Gemini worker startup path.
- A secondary validation risk was a flaky watcher test under full-suite load; that test was hardened to wait for watcher readiness and the full clean suite now passes.

## Final verdict

Release **0.8.3** is **ready to publish** based on the fresh local verification evidence above.