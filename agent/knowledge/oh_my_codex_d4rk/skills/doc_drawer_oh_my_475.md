o read
- `omx team api mailbox-mark-delivered --json` to acknowledge delivery

Copy/paste templates:

```bash
omx team api mailbox-list --input "{\"team_name\":\"<teamName>\",\"worker\":\"<workerName>\"}" --json
omx team api mailbox-mark-delivered --input "{\"team_name\":\"<teamName>\",\"worker\":\"<workerName>\",\"message_id\":\"<MESSAGE_ID>\"}" --json
```

## Dispatch Discipline (state-first)

Worker sessions should treat team state + CLI interop as the source of truth.

- Prefer inbox/mailbox/task state and `omx team api ... --json` operations.
- Do **not** rely on ad-hoc tmux keystrokes as a primary delivery channel.
- If a manual trigger arrives (for example `tmux send-keys` nudge), treat it only as a prompt to re-check state and continue through the normal claim-safe lifecycle.