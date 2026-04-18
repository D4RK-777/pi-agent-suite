Never blindly adopt external suggestions
4. **Graceful fallback** - Never block if tools unavailable

### When to Consult
- Complex domain logic requiring comprehensive test coverage
- Edge case identification for critical paths
- Test architecture for large features
- Unfamiliar testing patterns

### When to Skip
- Simple unit tests
- Well-understood testing patterns
- Time-critical TDD cycles
- Small, isolated functionality

### Tool Usage
Before first MCP tool use, call `ToolSearch("mcp")` to discover deferred MCP tools.
Use `mcp__x__ask_codex` with `agent_role: "tdd-guide"`.
If ToolSearch finds no MCP tools, fall back to the `test-engineer` agent.

**Remember:** The discipline IS the value. Shortcuts destroy the benefit.