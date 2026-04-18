**MUST** prefer durable state writes + runtime dispatch (`dispatch/requests.json`, mailbox, inbox).
- Direct tmux interaction is **fallback-only** and only after failure checks (for example `worker_notify_failed:<worker>`) or explicit user request (for example “press enter”).

## Operational Commands

```bash
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Semantics:

- `status`: reads team snapshot (task counts, dead/non-reporting workers)
- `resume`: reconnects to live team session if present
- `shutdown`: graceful shutdown request, then cleanup (deletes `.omx/state/team/<team>`)

## Data Plane and Control Plane

### Control Plane

- tmux panes/processes (`OMX_TEAM_WORKER` per worker)
- leader notifications via `tmux display-message`