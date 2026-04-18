eep the upgrade incremental and reversible, separate **signal collection** from **decision policy**:

1. **Allocation policy**
   - Input: decomposed tasks, routed roles, worker roster, dependency readiness, and current load.
   - Output: chosen owner, ranked fallbacks, and a short reason string.
   - Integration point: replace the round-robin-only decision inside `buildTeamExecutionPlan()` without changing task decomposition or role routing.

2. **Rebalance policy**
   - Input: the runtime snapshot inputs already assembled by `monitorTeam()`.
   - Output: structured actions (`noop`, `recommend`, `requeue`, `reassign`) plus rationale.
   - Integration point: let `monitorTeam()` compute richer actions, but keep `assignTask()` as the only real dispatch path.