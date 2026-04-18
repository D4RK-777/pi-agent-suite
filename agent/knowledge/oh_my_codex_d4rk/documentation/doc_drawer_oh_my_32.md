fig` / `--effort` para que Claude use el `settings.json` predeterminado.

## Qué escribe `omx setup`

- `.omx/setup-scope.json` (alcance de instalación persistido)
- Instalaciones dependientes del alcance:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Comportamiento de inicio: si el alcance persistido es `project`, el lanzamiento de `omx` usa automáticamente `CODEX_HOME=./.codex` (a menos que `CODEX_HOME` ya esté establecido).
- Las instrucciones de inicio combinan `~/.codex/AGENTS.md` (o `CODEX_HOME/AGENTS.md` si se sobrescribe) con `./AGENTS.md` del proyecto y luego añaden la superposición de runtime.