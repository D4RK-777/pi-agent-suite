`omx_run_team_cleanup` | Kill worker tmux panes for a job (early stop only) |

### CLI vs MCP Tools

- **`omx team ...` CLI** — Primary method for interactive team orchestration. Use this when you are operating inside a live tmux session and want direct pane visibility.
- **`omx_run_team_*` MCP tools** — For programmatic or agent-driven team spawning (analogous to OMC's `omc_run_team_*` tools). Use these when an agent needs to launch workers, poll status, and collect results without manual intervention.

### Naming Distinction

Two cleanup tools exist and must not be confused: