xt focus dimension.

### 2e) Persist state
Append round result and updated scores via `state_write`.

### 2f) Round controls
- Do not offer early exit before the first explicit assumption probe and one persistent follow-up have happened
- Round 4+: allow explicit early exit with risk warning
- Soft warning at profile midpoint (e.g., round 3/6/10 depending on profile)
- Hard cap at profile `max_rounds`

## Phase 3: Challenge Modes (assumption stress tests)

Use each mode once when applicable. These are normal escalation tools, not rare rescue moves: