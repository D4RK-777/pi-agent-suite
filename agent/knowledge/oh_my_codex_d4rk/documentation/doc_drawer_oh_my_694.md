val checks and post-claim rollback when worker notification fails (`src/team/runtime.ts:1426-1527`).

### Claim-safety invariants
- `claimTask()` can only move work into `in_progress` after dependency readiness succeeds and no active claim is held by another worker (`src/team/state/tasks.ts:56-113`).
- `transitionTaskStatus()` requires the active claim token before terminal completion/failure (`src/team/state/tasks.ts:132-200`).
- `releaseTaskClaim()` and `reclaimExpiredTaskClaim()` are the safe rollback/requeue paths; both clear owner + claim and return the task to `pending` (`src/team/state/tasks.ts:204-265`).

## Recommended policy seam

To keep the upgrade incremental and reversible, separate **signal collection** from **decision policy**: