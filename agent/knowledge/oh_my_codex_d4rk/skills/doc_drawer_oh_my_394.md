mux panes/processes (`OMX_TEAM_WORKER` per worker)
- leader notifications via `tmux display-message`

### Data Plane

- `.omx/state/team/<team>/...` files
- Team mailbox files:
- `.omx/state/team/<team>/mailbox/leader-fixed.json`
- `.omx/state/team/<team>/mailbox/worker-<n>.json`
- `.omx/state/team/<team>/dispatch/requests.json` (durable dispatch queue; hook-preferred, fallback-aware)

### Key Files