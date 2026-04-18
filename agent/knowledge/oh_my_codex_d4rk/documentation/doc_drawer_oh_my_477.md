re one idempotent shutdown path instead of duplicating raw transport bootstrap logic in each server.

This release:
- adds `autoStartStdioMcpServer` in `src/mcp/bootstrap.ts`
- migrates state, memory, code-intel, trace, and team MCP entrypoints to the shared helper
- routes stdin close, transport close, `SIGTERM`, and `SIGINT` through one lifecycle path
- adds regression coverage for idle teardown across the MCP server entrypoints

PRs: [#626](https://github.com/Yeachan-Heo/oh-my-codex/pull/626), [#627](https://github.com/Yeachan-Heo/oh-my-codex/pull/627)

### npm global-install bin contract fix

This release also includes a last-minute packaging fix for global installation behavior.