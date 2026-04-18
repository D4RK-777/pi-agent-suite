tools.

```bash
omx team api <operation> --input '{"team_name":"my-team",...}' --json
```

Examples:

```bash
omx team api send-message --input '{"team_name":"my-team","from_worker":"worker-1","to_worker":"leader-fixed","body":"ACK"}' --json
omx team api claim-task --input '{"team_name":"my-team","task_id":"1","worker":"worker-1"}' --json
omx team api transition-task-status --input '{"team_name":"my-team","task_id":"1","from":"in_progress","to":"completed","claim_token":"<token>"}' --json
```

`--json` responses include stable metadata for automation:
- `schema_version`
- `timestamp`
- `command`
- `ok`
- `operation`
- `data` or `error`

## Team + Worker Protocol Notes

Leader-to-worker:

- Write full assignment to worker `inbox.md`
- Send short trigger (<200 chars) with `tmux send-keys`