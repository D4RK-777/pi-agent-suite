4. Rebuild if running repo-local (`npm run build`)

### Team starts but leader gets no ACK

Checks:

1. Worker pane capture shows inbox processing
2. `.omx/state/team/<team>/mailbox/leader-fixed.json` exists
3. Worker skill loaded and `omx team api send-message --json` called
4. Task-id mismatch not blocking worker flow

### Worker logs `omx team api ... ENOENT` (or legacy `team_send_message ENOENT` / `team_update_task ENOENT`)

Meaning:
- Team state path no longer exists while worker is still running.
- Typical cause: leader/manual flow ran `omx team shutdown <team>` (or removed `.omx/state/team/<team>`) before worker finished.

Checks: