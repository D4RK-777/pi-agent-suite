okens`, `total-input-tokens`, `total-output-tokens`, `session-id`

## Layer 2: OMX Orchestration HUD

The `omx hud` command reads these state files:
- `.omx/state/ralph-state.json` - Ralph loop iteration
- `.omx/state/ultrawork-state.json` - Ultrawork mode
- `.omx/state/autopilot-state.json` - Autopilot phase
- `.omx/state/team-state.json` - Team workers
- `.omx/state/pipeline-state.json` - Pipeline stage
- `.omx/state/ecomode-state.json` - Ecomode active
- `.omx/state/hud-state.json` - Last activity (from notify hook)
- `.omx/metrics.json` - Turn counts

## Configuration

HUD config stored at `.omx/hud-config.json`:
```json
{
  "preset": "focused"
}
```

## Color Coding

- **Green**: Normal/healthy
- **Yellow**: Warning (ralph >70% of max)
- **Red**: Critical (ralph >90% of max)