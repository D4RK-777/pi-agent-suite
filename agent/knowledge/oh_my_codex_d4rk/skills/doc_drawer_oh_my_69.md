ity check
   - Code-reviewer: Quality review
   - All must approve; fix and re-validate on rejection

6. **Phase 5 - Cleanup**: Clear all mode state via OMX MCP tools on successful completion
   - `state_clear({mode: "autopilot"})`
   - `state_clear({mode: "ralph"})`
   - `state_clear({mode: "ultrawork"})`
   - `state_clear({mode: "ultraqa"})`
   - Or run `/cancel` for clean exit
</Steps>

<Tool_Usage>
- Before first MCP tool use, call `ToolSearch("mcp")` to discover deferred MCP tools
- Use `ask_codex` with `agent_role: "architect"` for Phase 4 architecture validation
- Use `ask_codex` with `agent_role: "security-reviewer"` for Phase 4 security review
- Use `ask_codex` with `agent_role: "code-reviewer"` for Phase 4 quality review