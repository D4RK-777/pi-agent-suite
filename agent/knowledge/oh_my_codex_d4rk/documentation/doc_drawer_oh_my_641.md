o cross-session corruption,
  - gate scenarios V1–V10 stay green in CI.

## Verification matrix gate

| ID | Scenario | Required evidence | Status |
|---|---|---|---|
| V1 | Session-scoped Ralph lifecycle | `src/cli/__tests__/session-scoped-runtime.test.ts` + `src/mcp/__tests__/trace-server.test.ts` | [x] |
| V2 | Root fallback compatibility (HUD) | `src/hud/__tests__/state.test.ts` | [x] |
| V3 | Canonical PRD/progress precedence + migration | `src/ralph/__tests__/persistence.test.ts` | [x] |
| V4 | Phase vocabulary enforcement | `src/mcp/__tests__/state-server-ralph-phase.test.ts` | [x] |
| V5 | Cancel standalone Ralph terminalization | `src/cli/__tests__/session-scoped-runtime.test.ts` | [x] |