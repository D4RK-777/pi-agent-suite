# Ralph Upstream → OMX Parity Matrix

Baseline source: `docs/reference/ralph-upstream-baseline.md` (`165c3688bfde275560c001a0de4c7563cf82ad69`)

| Rule ID | Upstream semantic rule | OMX implementation point(s) | Status | Verification reference |
|---|---|---|---|---|
| R1 | Ralph iterations are persisted (`iteration`, `max_iterations`, phase progression). | `src/mcp/state-server.ts` (`state_write`), `src/cli/__tests__/session-scoped-runtime.test.ts` | adopted | V1, V4 |
| R2 | Legacy phase labels must be normalized to canonical Ralph phases. | `src/mcp/state-server.ts` (Ralph phase normalizer), `src/mcp/__tests__/state-server-ralph-phase.test.ts` | adapted | V4 |