pat.test.ts:47-170`
- `src/hud/state.ts:107-123`
- `src/team/api-interop.ts:432-436`

Current state:

- compatibility readers intentionally preserve legacy/current precedence
- this is useful for migration safety, but it keeps the read path more complex than the target architecture

Risk:

- future format drift can hide inside fallback behavior instead of failing at a single canonical reader boundary

Desired end state:

- compatibility readers keep only the minimum fallback behavior still required by supported migration lanes
- newer paths read one canonical Rust-authored surface first

## Recommended follow-up order

1. Collapse team state-root / working-directory resolution to one canonical metadata source
2. Reduce compatibility fallback layers after the write path is single-owner