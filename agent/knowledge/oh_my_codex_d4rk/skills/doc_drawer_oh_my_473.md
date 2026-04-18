`<team_state_root>/team/<teamName>/tasks/task-<id>.json` (example: `task-1.json`)
5. Task id format:
   - The MCP/state API uses the numeric id (`"1"`), not `"task-1"`.
   - Never use legacy `tasks/{id}.json` wording.
6. Claim the task (do NOT start work without a claim) using claim-safe lifecycle CLI interop (`omx team api claim-task --json`).
7. Do the work.
8. Complete/fail the task via lifecycle transition CLI interop (`omx team api transition-task-status --json`) from `in_progress` to `completed` or `failed`.
   - Do NOT directly write lifecycle fields (`status`, `owner`, `result`, `error`) in task files.
9. Use `omx team api release-task-claim --json` only for rollback/requeue to `pending` (not for completion).
10. Update your worker status: