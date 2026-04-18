team spawning (as opposed to interactive CLI use), OMX exposes four MCP tools via the `team-server`:

| Tool | Description |
|------|-------------|
| `omx_run_team_start` | Spawn tmux CLI workers in the background; returns a `jobId` immediately |
| `omx_run_team_status` | Non-blocking status check for a running job |
| `omx_run_team_wait` | Block until the job completes, with automatic idle-pane nudging |
| `omx_run_team_cleanup` | Kill worker tmux panes for a job (early stop only) |

### CLI vs MCP Tools