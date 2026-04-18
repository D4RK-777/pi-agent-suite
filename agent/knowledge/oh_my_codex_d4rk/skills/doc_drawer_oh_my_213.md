ultrawork, autopilot, team, pipeline, ecomode, turns). Reads `.omx/state/` files.

## Quick Commands

| Command | Description |
|---------|-------------|
| `omx hud` | Show current HUD (modes, turns, activity) |
| `omx hud --watch` | Live-updating display (polls every 1s) |
| `omx hud --json` | Raw state output for scripting |
| `omx hud --preset=minimal` | Minimal display |
| `omx hud --preset=focused` | Default display |
| `omx hud --preset=full` | All elements |

## Presets

### minimal
```
[OMX] ralph:3/10 | turns:42
```

### focused (default)
```
[OMX] ralph:3/10 | ultrawork | team:3 workers | turns:42 | last:5s ago
```

### full
```
[OMX] ralph:3/10 | ultrawork | autopilot:execution | team:3 workers | pipeline:exec | turns:42 | last:5s ago | total-turns:156
```

## Setup