eam>/dispatch/requests.json` (durable dispatch queue; hook-preferred, fallback-aware)

### Key Files

- `.omx/state/team/<team>/config.json`
- `.omx/state/team/<team>/manifest.v2.json`
- `.omx/state/team/<team>/tasks/task-<id>.json`
- `.omx/state/team/<team>/workers/worker-<n>/identity.json`
- `.omx/state/team/<team>/workers/worker-<n>/inbox.md`
- `.omx/state/team/<team>/workers/worker-<n>/heartbeat.json`
- `.omx/state/team/<team>/workers/worker-<n>/status.json`
- `.omx/state/team-leader-nudge.json`


## Team Mutation Interop (CLI-first)

Use `omx team api` for machine-readable mutation/reads instead of legacy `team_*` MCP tools.

```bash
omx team api <operation> --input '{"team_name":"my-team",...}' --json
```

Examples: