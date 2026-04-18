on`
- `.omx/state/plan-consensus.json`
- `.omx/state/ralplan-state.json`
- `.omx/state/boulder.json`
- `.omx/state/hud-state.json`
- `.omx/state/subagent-tracking.json`
- `.omx/state/subagent-tracker.lock`
- `.omx/state/rate-limit-daemon.pid`
- `.omx/state/rate-limit-daemon.log`
- `.omx/state/checkpoints/` (directory)
- `.omx/state/sessions/` (empty directory cleanup after clearing sessions)

## Implementation Steps

When you invoke this skill:

### 1. Parse Arguments

```bash
# Check for --force or --all flags
FORCE_MODE=false
if [[ "$*" == *"--force"* ]] || [[ "$*" == *"--all"* ]]; then
  FORCE_MODE=true
fi
```

### 2. Detect Active Modes