r active teams
ls .omx/state/team/*/config.json 2>/dev/null
```

**Two-pass cancellation protocol:**

**Pass 1: Graceful Shutdown**
```
For each team found in .omx/state/team/:
  1. Read config.json to get team_name and workers list
  2. For each worker:
     a. Write shutdown inbox to .omx/state/team/{name}/workers/{worker}/inbox.md
     b. Send short trigger via tmux send-keys
     c. Wait up to 15 seconds for worker tmux pane to exit
     d. If still alive: mark as unresponsive
```

**Pass 2: Force Kill**
```
After graceful pass:
  1. For each remaining alive worker:
     a. Send C-c via tmux send-keys
     b. Wait 2 seconds
     c. Kill the tmux window if still alive
  2. Destroy the tmux session: tmux kill-session -t omx-team-{name}
```