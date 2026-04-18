Überschreibungen, sodass Claude die Standard-`settings.json` verwendet.

## Was `omx setup` schreibt

- `.omx/setup-scope.json` (persistierter Setup-Bereich)
- Bereichsabhängige Installationen:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Startverhalten: Wenn der persistierte Bereich `project` ist, verwendet `omx` automatisch `CODEX_HOME=./.codex` (sofern `CODEX_HOME` nicht bereits gesetzt ist).
- Startanweisungen kombinieren `~/.codex/AGENTS.md` (bzw. `CODEX_HOME/AGENTS.md`, wenn überschrieben) mit dem Projekt-`./AGENTS.md` und hängen anschließend die Runtime-Überlagerung an.