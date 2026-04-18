hout manual intervention.

### Naming Distinction

Two cleanup tools exist and must not be confused:

- `team_cleanup` (**state-server**): Deletes team state **files** on disk (`.omx/state/team/<team>/`). Use after a team run is fully complete.
- `omx_run_team_cleanup` (**team-server**): Kills tmux worker **panes** for a job. Use only when stopping workers early; otherwise `omx_run_team_wait` handles natural termination.

### Basic Usage Example

```
1. omx_run_team_start({
     teamName: "fix-bugs",
     agentTypes: ["codex"],
     tasks: [{ subject: "Fix bug", description: "..." }],
     cwd: "/path/to/project"
   })
   → Returns { jobId: "omx-abc123" }

2. omx_run_team_wait({ job_id: "omx-abc123", timeout_ms: 300000 })
   → Blocks until done, auto-nudges idle panes