task-claim --json` only for rollback/requeue-to-pending flows.

## Legacy MCP -> CLI migration table

| Legacy `team_*` tool | CLI operation |
|---|---|
| `team_send_message` | `omx team api send-message --json` |
| `team_broadcast` | `omx team api broadcast --json` |
| `team_mailbox_list` | `omx team api mailbox-list --json` |
| `team_mailbox_mark_notified` | `omx team api mailbox-mark-notified --json` |
| `team_mailbox_mark_delivered` | `omx team api mailbox-mark-delivered --json` |
| `team_create_task` | `omx team api create-task --json` |
| `team_read_task` | `omx team api read-task --json` |
| `team_list_tasks` | `omx team api list-tasks --json` |
| `team_update_task` | `omx team api update-task --json` |
| `team_claim_task` | `omx team api claim-task --json` |