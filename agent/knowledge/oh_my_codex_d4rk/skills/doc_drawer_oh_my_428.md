, and test suites use `run_in_background: true`
7. **Verify when all tasks complete** (lightweight):
   - Build/typecheck passes
   - Affected tests pass
   - No new errors introduced
</Steps>

<Tool_Usage>
- Use LOW-tier delegation for simple changes
- Use STANDARD-tier delegation for standard work
- Use THOROUGH-tier delegation for complex work
- Use `run_in_background: true` for package installs, builds, and test suites
- Use foreground execution for quick status checks and file operations
</Tool_Usage>

## State Management

Use `omx_state` MCP tools for ultrawork lifecycle state.