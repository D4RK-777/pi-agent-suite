se 4 security review
- Use `ask_codex` with `agent_role: "code-reviewer"` for Phase 4 quality review
- Agents form their own analysis first, then consult Codex for cross-validation
- If ToolSearch finds no MCP tools or Codex is unavailable, proceed without it -- never block on external tools
</Tool_Usage>

## State Management

Use `omx_state` MCP tools for autopilot lifecycle state.

- **On start**:
  `state_write({mode: "autopilot", active: true, current_phase: "expansion", started_at: "<now>", state: {context_snapshot_path: "<snapshot-path>"}})`
- **On phase transitions**:
  `state_write({mode: "autopilot", current_phase: "planning"})`
  `state_write({mode: "autopilot", current_phase: "execution"})`
  `state_write({mode: "autopilot", current_phase: "qa"})`