, `~/.omx/agents`)
  - `project`: local directories (`./.codex`, `./.codex/skills`, `./.omx/agents`)
- Migration hint: in `user` scope, if historical `~/.agents/skills` still exists alongside `${CODEX_HOME:-~/.codex}/skills`, current setup prints a cleanup hint because Codex may show duplicate skill entries until the legacy tree is removed or archived.
- If persisted scope is `project`, `omx` launch automatically uses `CODEX_HOME=./.codex` unless user explicitly overrides `CODEX_HOME`.
- With `--force`, AGENTS overwrite may still be skipped if an active OMX session is detected (safety guard).
- Legacy persisted scope values (`project-local`) are automatically migrated to `project` with a one-time warning.

## Recommended workflow

1. Run setup:

```bash
omx setup --force --verbose
```