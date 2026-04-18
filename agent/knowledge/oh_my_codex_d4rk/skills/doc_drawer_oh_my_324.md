ode
- Well-audited patterns
- Time-critical security assessments
- Code with existing security tests

### Tool Usage
Before first MCP tool use, call `ToolSearch("mcp")` to discover deferred MCP tools.
Use `mcp__x__ask_codex` with `agent_role: "security-reviewer"`.
If ToolSearch finds no MCP tools, fall back to the `security-reviewer` agent.

**Note:** Security second opinions are high-value. Consider consulting for CRITICAL/HIGH findings.

## Output Format

```
SECURITY REVIEW REPORT
======================

Scope: Entire codebase (42 files scanned)
Scan Date: 2026-01-24T14:30:00Z