, lsp_prepare_rename, lsp_rename, lsp_code_actions, lsp_code_action_resolve (5 tools need real LSP).
6. **Python REPL** - Not yet ported. Needed only by scientist agent. Low priority for v0.1.0.

## Upstream Contribution Path

To achieve 100% hook parity, these changes need to be contributed to Codex CLI:
1. Add `BeforeToolUse` hook event to `codex-rs/hooks/`
2. Add `UserPromptSubmit` hook event
3. Add external hook configuration in `config.toml` (currently only `notify`)
4. Add hook context injection (hook stdout -> system message)

RFC tracking: TBD