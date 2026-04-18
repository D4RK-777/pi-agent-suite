worker/SKILL.md`
4. `<leader_cwd>/skills/worker/SKILL.md` (repo fallback)

## Startup Protocol (ACK)

1. Parse `OMX_TEAM_WORKER` into:
   - `teamName` (before the `/`)
   - `workerName` (after the `/`, usually `worker-<n>`)
2. Send a startup ACK to the lead mailbox **before task work**:
   - Recipient worker id: `leader-fixed`
   - Body: one short deterministic line (recommended: `ACK: <workerName> initialized`).
3. After ACK, proceed to your inbox instructions.

The lead will see your message in:

`<team_state_root>/team/<teamName>/mailbox/leader-fixed.json`

Use CLI interop:
- `omx team api send-message --input <json> --json` with `{team_name, from_worker, to_worker:"leader-fixed", body}`

Copy/paste template: