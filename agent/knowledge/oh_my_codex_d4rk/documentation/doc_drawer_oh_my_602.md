am execution
  - use `omx ralph ...` separately if a later persistent follow-up loop is still needed

## Notable implementation areas
- `src/cli/team.ts`
- `src/cli/index.ts`
- `src/team/runtime.ts`
- `src/team/runtime-cli.ts`
- `src/team/api-interop.ts`
- `src/team/state.ts`
- `src/team/state/types.ts`
- `src/scripts/notify-hook.ts`
- `src/team/followup-planner.ts`
- `src/pipeline/stages/team-exec.ts`

## Deleted surfaces
- `src/team/linked-ralph-bridge.ts`
- `src/scripts/notify-hook/linked-sync.ts`
- `src/cli/__tests__/team-linked-ralph.test.ts`
- `src/team/__tests__/linked-ralph-bridge.test.ts`
- `src/hooks/__tests__/notify-hook-linked-sync.test.ts`