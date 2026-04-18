all state files
9. **On rejection**: Fix the issues raised, then re-verify at the same tier
</Steps>

<Tool_Usage>
- Before first MCP tool use, call `ToolSearch("mcp")` to discover deferred MCP tools
- Use `ask_codex` with `agent_role: "architect"` for verification cross-checks when changes are security-sensitive, architectural, or involve complex multi-system integration
- Skip Codex consultation for simple feature additions, well-tested changes, or time-critical verification
- If ToolSearch finds no MCP tools or Codex is unavailable, proceed with architect agent verification alone -- never block on external tools
- Use `state_write` / `state_read` for ralph mode state persistence between iterations