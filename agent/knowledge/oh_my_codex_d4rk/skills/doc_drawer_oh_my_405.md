ss but stale worker panes remain

Cause:
- stale pane outside config tracking or previous failed run

Fix:
- manual pane cleanup (see clean-slate commands)

## Clean-Slate Recovery

Run from leader pane:

```bash
# 1) Inspect panes
tmux list-panes -F '#{pane_id}\t#{pane_current_command}\t#{pane_start_command}'

# 2) Kill stale worker panes only (examples)
tmux kill-pane -t %450
tmux kill-pane -t %451

# 3) Remove stale team state (example)
rm -rf .omx/state/team/<team-name>

# 4) Retry
omx team 1:executor "fresh retry"
```

Guidelines:

- Do not kill leader pane
- Do not kill HUD pane (`omx hud --watch`) unless intentionally restarting HUD

## Required Reporting During Execution

When operating this skill, provide concrete progress evidence: