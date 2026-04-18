/team/__tests__/linked-ralph-bridge.test.ts`
- `src/hooks/__tests__/notify-hook-linked-sync.test.ts`

## Impact
### Before
- `omx team ralph ...` had special runtime behavior
- team state could carry linked Ralph metadata
- notify-hook and shutdown logic had linked team↔Ralph branches
- docs/planning artifacts promoted a built-in linked verification path

### After
- `omx team ...` runs coordinated team execution only
- team owns its own verification lanes and shutdown evidence
- `omx ralph ...` is separate and explicit
- a leader or separate worker may still choose to run Ralph later
- there is no built-in linked team+Ralph lifecycle anymore