the runtime auto-commits as a fallback, but explicit commits are preferred

Task ID rule (critical):

- File path uses `task-<id>.json` (example `task-1.json`)
- MCP API `task_id` uses bare id (example `"1"`, not `"task-1"`)
- Never instruct workers to read `tasks/{id}.json`

## Environment Knobs

Useful runtime env vars:

- `OMX_TEAM_READY_TIMEOUT_MS`
  - Worker readiness timeout (default 45000)
- `OMX_TEAM_SKIP_READY_WAIT=1`
  - Skip readiness wait (debug only)
- `OMX_TEAM_AUTO_TRUST=0`
  - Disable auto-advance for trust prompt (default behavior auto-advances)
- `OMX_TEAM_AUTO_ACCEPT_BYPASS=0`
  - Disable Claude bypass-permissions prompt auto-accept (default behavior auto-accepts `2` + Enter)
- `OMX_TEAM_WORKER_LAUNCH_ARGS`
  - Extra args passed to worker launch command