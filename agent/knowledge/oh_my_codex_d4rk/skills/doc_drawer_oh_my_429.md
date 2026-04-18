rations
</Tool_Usage>

## State Management

Use `omx_state` MCP tools for ultrawork lifecycle state.

- **On start**:
  `state_write({mode: "ultrawork", active: true, reinforcement_count: 1, started_at: "<now>"})`
- **On each reinforcement/loop step**:
  `state_write({mode: "ultrawork", reinforcement_count: <current>})`
- **On completion**:
  `state_write({mode: "ultrawork", active: false})`
- **On cancellation/cleanup**:
  run `$cancel` (which should call `state_clear(mode="ultrawork")`)