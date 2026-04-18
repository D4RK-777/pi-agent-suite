<json> --json` with `{team_name, from_worker, to_worker:"leader-fixed", body}`

Copy/paste template:

```bash
omx team api send-message --input "{\"team_name\":\"<teamName>\",\"from_worker\":\"<workerName>\",\"to_worker\":\"leader-fixed\",\"body\":\"ACK: <workerName> initialized\"}" --json
```

## Inbox + Tasks

1. Resolve canonical team state root in this order:
   1) `OMX_TEAM_STATE_ROOT` env
   2) worker identity `team_state_root`
   3) team config/manifest `team_state_root`
   4) local cwd fallback (`.omx/state`)
2. Read your inbox:
   `<team_state_root>/team/<teamName>/workers/<workerName>/inbox.md`
3. Pick the first unblocked task assigned to you.
4. Read the task file:
   `<team_state_root>/team/<teamName>/tasks/task-<id>.json` (example: `task-1.json`)
5. Task id format: