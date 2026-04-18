ship work is outside dispatch/mailbox and focuses on broader metadata/fallback simplification

Risk:

- contributors may still misread broader metadata/fallback layers as ownership layers if the docs are not kept precise
- future compatibility work could accidentally reintroduce JS canonical writes without contract/test coverage

Desired end state:

- Rust is the sole semantic owner for runtime state transitions
- TS remains a thin reader / delivery adapter only

### 4. Compatibility readers still carry fallback precedence logic

Evidence:

- `src/compat/__tests__/rust-runtime-compat.test.ts:47-170`
- `src/hud/state.ts:107-123`
- `src/team/api-interop.ts:432-436`

Current state: