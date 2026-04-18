p when existing and no force)
6. Configure notify hook references and write `./.omx/hud-config.json`

## Important behavior notes

- `omx setup` only prompts for scope when no scope is provided/persisted and stdin/stdout are TTY.
- Local project orchestration file is `./AGENTS.md` (project root).
- If `AGENTS.md` exists and `--force` is not used, interactive TTY runs ask whether to overwrite. Non-interactive runs preserve the file.
- Scope targets:
  - `user`: user directories (`~/.codex`, `~/.codex/skills`, `~/.omx/agents`)
  - `project`: local directories (`./.codex`, `./.codex/skills`, `./.omx/agents`)