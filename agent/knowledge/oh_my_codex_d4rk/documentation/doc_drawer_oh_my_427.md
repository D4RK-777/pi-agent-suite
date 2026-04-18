s dist/hooks/__tests__/notify-hook-auto-nudge.test.js dist/hooks/__tests__/agents-overlay.test.js` ✅
- `node --test --test-reporter=spec dist/hud/__tests__/index.test.js dist/hud/__tests__/render.test.js dist/hud/__tests__/state.test.js` ✅
- `node --test --test-reporter=spec dist/pipeline/__tests__/stages.test.js dist/ralplan/__tests__/runtime.test.js` ✅

## Remaining risk

- This release verification is intentionally targeted to the post-`0.11.8` surfaces that changed; it is not a full GitHub Actions matrix rerun.
- Future nudge entrypoints must preserve the same deep-interview lock suppression check to keep the behavior consistent.
- Future HUD / pipeline readers should preserve the new ralplan runtime field names if they depend on the live observability surface.