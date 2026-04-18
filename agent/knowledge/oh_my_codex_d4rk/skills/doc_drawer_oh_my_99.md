e tmux window if still alive
  2. Destroy the tmux session: tmux kill-session -t omx-team-{name}
```

**Cleanup:**
```
  1. Strip AGENTS.md team worker overlay (<!-- OMX:TEAM:WORKER:START/END -->)
  2. Remove team state directory: rm -rf .omx/state/team/{name}/
  3. Clear team mode state: state_clear(mode="team")
  4. Emit structured cancel report
```

**Structured Cancel Report:**
```
Team "{team_name}" cancelled:
  - Workers signaled: N
  - Graceful exits: M
  - Force killed: K
  - tmux session destroyed: yes/no
  - State cleaned up: yes/no
```