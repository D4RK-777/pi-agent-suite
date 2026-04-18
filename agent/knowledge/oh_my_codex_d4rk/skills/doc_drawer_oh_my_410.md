am_wait({ job_id: "omx-abc123", timeout_ms: 300000 })
   → Blocks until done, auto-nudges idle panes

3. omx_run_team_cleanup({ job_id: "omx-abc123" })
   → Only needed if stopping workers early
```

`omx_run_team_status` can be called between steps 1 and 2 for a non-blocking poll if you need to interleave other work while workers run.

## Limitations

- Worktree provisioning requires a git repository and can fail on branch/path collisions
- send-keys interactions can be timing-sensitive under load
- stale panes from prior runs can interfere until manually cleaned

## Scenario Examples

**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.