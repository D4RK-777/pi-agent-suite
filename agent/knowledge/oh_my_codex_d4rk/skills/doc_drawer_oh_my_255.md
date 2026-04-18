egration/e2e/observability)

Plans are saved to `.omx/plans/`. Drafts go to `.omx/drafts/`.
</Steps>

<Tool_Usage>
- Before first MCP tool use, call `ToolSearch("mcp")` to discover deferred MCP tools
- Use `AskUserQuestion` for preference questions (scope, priority, timeline, risk tolerance) -- provides clickable UI
- Use plain text for questions needing specific values (port numbers, names, follow-up clarifications)
- Use the `explore` agent (LOW tier, bounded quick pass) to gather codebase facts before asking the user
- Use `ask_codex` with `agent_role: "planner"` for planning validation on large-scope plans
- Use `ask_codex` with `agent_role: "analyst"` for requirements analysis
- Use `ask_codex` with `agent_role: "critic"` for plan review in consensus and review modes