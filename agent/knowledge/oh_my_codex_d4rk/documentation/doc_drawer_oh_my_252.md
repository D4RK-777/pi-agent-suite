/state/team/...` are unsupported and may violate runtime invariants.

## Required task mutation flow

1. Read current task:
   - `omx team api read-task --json`
2. Claim with optimistic version:
   - `omx team api claim-task --json`
3. Transition terminal state with claim token:
   - `omx team api transition-task-status --json` (`in_progress -> completed|failed`)
4. Use `omx team api release-task-claim --json` only for rollback/requeue-to-pending flows.

## Legacy MCP -> CLI migration table