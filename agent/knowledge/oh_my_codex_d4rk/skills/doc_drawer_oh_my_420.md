al met after 2 cycles
```

## State Tracking

Use `omx_state` MCP tools for UltraQA lifecycle state.

- **On start**:
  `state_write({mode: "ultraqa", active: true, current_phase: "qa", iteration: 1, started_at: "<now>"})`
- **On each cycle**:
  `state_write({mode: "ultraqa", current_phase: "qa", iteration: <cycle>})`
- **On diagnose/fix transitions**:
  `state_write({mode: "ultraqa", current_phase: "diagnose"})`
  `state_write({mode: "ultraqa", current_phase: "fix"})`
- **On completion**:
  `state_write({mode: "ultraqa", active: false, current_phase: "complete", completed_at: "<now>"})`
- **For resume detection**:
  `state_read({mode: "ultraqa"})`


## Scenario Examples