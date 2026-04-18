king-directory or state-root resolution can depend on fallback order instead of one canonical source

Desired end state:

- one canonical metadata source for team state-root / working-directory resolution
- the remaining files become derived compatibility views only

### 3. Runtime ownership contract vs. cutover reality

Status: **resolved by issue #1108 for dispatch/mailbox ownership**

Evidence:

- `src/runtime/bridge.ts:2-6`
- `src/team/state/dispatch.ts:130-140`
- `src/team/state/mailbox.ts:45-49`

Current state:

- the bridge contract and the team dispatch/mailbox write paths now agree on Rust ownership
- remaining ownership work is outside dispatch/mailbox and focuses on broader metadata/fallback simplification

Risk: