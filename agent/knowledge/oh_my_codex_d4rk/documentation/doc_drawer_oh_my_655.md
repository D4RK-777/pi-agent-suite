dist/hooks/__tests__/notify-fallback-watcher.test.js` | PASS (`6` pass / `0` fail) |

## Risk notes

- This is a focused patch release centered on `omx setup` refresh behavior and managed model upgrade prompting.
- Primary regression surface is setup/config refresh behavior across repeat runs and scoped installs.
- Release validation uncovered two additional quality issues during final gating: a watcher shutdown cleanup race in one streaming test and an unused setup prompt path caught by the strict no-unused check. Both were resolved and the full release gates were rerun cleanly.

## Final verdict

Release **0.8.4** is **ready to publish** based on the fresh local verification evidence above.