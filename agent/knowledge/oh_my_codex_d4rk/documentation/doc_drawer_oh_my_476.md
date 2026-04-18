ardening pass focused on expired-claim recovery, worktree hygiene, and stronger regression coverage.

Notable effects:
- safer claim recovery behavior when leases expire
- better worktree cleanup and hygiene paths
- broader runtime/state/worktree/end-to-end regression coverage
- a dedicated hardening benchmark script

PR: [#624](https://github.com/Yeachan-Heo/oh-my-codex/pull/624)

### MCP server stdio teardown unification

OMX's MCP stdio entrypoints now share one idempotent shutdown path instead of duplicating raw transport bootstrap logic in each server.