est.ts`, `src/notifications/__tests__/tmux-detector.test.ts` | [x] |

## Pre-mortem scenario mapping

| Pre-mortem scenario | Gate(s) |
|---|---|
| Semantic leakage survives into legacy readers | G1, G2, G3, G4 |
| Reader precedence drifts between config/manifest or session/root scopes | G1, G2, G3 |
| Watcher send-keys parity breaks | G5 |
| Mux contract stays tmux-shaped instead of Rust-canonical | G4 |

## Required docs

- `docs/contracts/rust-runtime-thin-adapter-contract.md`
- `docs/interop-team-mutation-contract.md`
- `docs/qa/runtime-team-seam-audit-2026-04-01.md` (non-gating follow-up seam snapshot)

## Non-gating follow-up audit