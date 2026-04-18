xternal tools
- Use `state_write` / `state_read` for ralph mode state persistence between iterations
- Persist context snapshot path in Ralph mode state so later phases and agents share the same grounding context
</Tool_Usage>

## State Management

Use the `omx_state` MCP server tools (`state_write`, `state_read`, `state_clear`) for Ralph lifecycle state.

- **On start**:
  `state_write({mode: "ralph", active: true, iteration: 1, max_iterations: 10, current_phase: "executing", started_at: "<now>", state: {context_snapshot_path: "<snapshot-path>"}})`
- **On each iteration**:
  `state_write({mode: "ralph", iteration: <current>, current_phase: "executing"})`
- **On verification/fix transition**: