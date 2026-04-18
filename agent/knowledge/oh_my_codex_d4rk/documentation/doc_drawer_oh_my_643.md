`src/verification/__tests__/ralph-persistence-gate.test.ts` | [x] |

### Explicit scenario checklist

- [x] V1 Session-scoped Ralph lifecycle
- [x] V2 Root fallback compatibility (HUD)
- [x] V3 Canonical PRD/progress precedence + migration
- [x] V4 Phase vocabulary enforcement
- [x] V5 Cancel standalone Ralph terminalization
- [x] V6 Cancel Ralph linked mode behavior
- [x] V7 Team-linked terminal propagation
- [x] V8 Cross-session safety
- [x] V9 Upstream parity evidence
- [x] V10 CI/release gate enforcement

## Required docs

- `docs/contracts/ralph-state-contract.md`
- `docs/contracts/ralph-cancel-contract.md`
- `docs/reference/ralph-upstream-baseline.md`
- `docs/reference/ralph-parity-matrix.md`

## Release note requirements

Every release touching Ralph persistence MUST mention: