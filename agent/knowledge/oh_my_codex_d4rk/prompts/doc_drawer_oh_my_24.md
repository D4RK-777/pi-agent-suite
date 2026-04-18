ommands
omx team status "$TEAM_NAME"
omx team resume "$TEAM_NAME"
omx team shutdown "$TEAM_NAME"
```

**Expected:**
- Team starts with 5+ workers and prints `Team started: <team-name>` plus worker counts.
- Mixed CLI map runs Codex workers and Claude workers in one team.
- `status` shows task distribution and worker health.
- `shutdown` cleans up workers and team state.

## Demo 7: `omx team api` Rich CLI Interop Demonstration

All mutations should use CLI interop (`omx team api ... --json`) with the stable JSON envelope.

### 7.1 Task lifecycle (claim-safe)