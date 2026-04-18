# Team Allocation and Rebalance Policy Notes

This note documents the current team-mode allocation/rebalance seam and the constraints that the phased allocation/rebalance upgrade must preserve.

## Current baseline

### Startup allocation
- `buildTeamExecutionPlan()` splits the top-level request, routes each subtask to a role, then assigns owners via `distributeTasksToWorkers()`.
- Ownership now flows through `allocateTasksToWorkers()` so startup assignment stays lane-aware instead of pure round-robin (`src/cli/team.ts`, `src/team/allocation-policy.ts`).
- The current heuristic keeps same-role work grouped when possible, prefers explicit worker-role matches, and falls back to load balancing with lighter-lane bias for blocked work.