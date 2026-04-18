--json` only for rollback/requeue to `pending` (not for completion).
10. Update your worker status:
   `<team_state_root>/team/<teamName>/workers/<workerName>/status.json` with `{"state":"idle", ...}`

## Mailbox

Check your mailbox for messages:

`<team_state_root>/team/<teamName>/mailbox/<workerName>.json`

When notified, read messages and follow any instructions. Use short ACK replies when appropriate.

Note: leader dispatch is state-first. The durable queue lives at:
`<team_state_root>/team/<teamName>/dispatch/requests.json`
Hooks/watchers may nudge you after mailbox/inbox state is already written.

Use CLI interop:
- `omx team api mailbox-list --json` to read
- `omx team api mailbox-mark-delivered --json` to acknowledge delivery

Copy/paste templates: