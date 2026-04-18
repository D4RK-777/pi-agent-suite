orker may still choose to run Ralph later
- there is no built-in linked team+Ralph lifecycle anymore

## Validation
- [x] `npm run build`
- [x] targeted tests covering CLI parsing, runtime/state behavior, team API interop, planner handoff generation, and hook/contract expectations

Verification command:
```bash
npm run build && node --test   dist/cli/__tests__/team.test.js   dist/team/__tests__/followup-planner.test.js   dist/pipeline/__tests__/stages.test.js   dist/hooks/__tests__/keyword-detector.test.js   dist/hooks/__tests__/consensus-execution-handoff.test.js   dist/hooks/__tests__/deep-interview-contract.test.js   dist/team/__tests__/runtime.test.js   dist/team/__tests__/state.test.js   dist/team/__tests__/api-interop.test.js
```

Result:
- `428 pass, 0 fail`