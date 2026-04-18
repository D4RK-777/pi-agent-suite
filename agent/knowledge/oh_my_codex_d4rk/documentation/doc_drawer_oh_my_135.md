` / `--effort`, чтобы Claude использовал стандартный `settings.json`.

## Что записывает `omx setup`

- `.omx/setup-scope.json` (сохранённая область установки)
- Установки в зависимости от области:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Поведение при запуске: если сохранённая область — `project`, `omx` автоматически использует `CODEX_HOME=./.codex` (если `CODEX_HOME` ещё не задан).
- Инструкции запуска объединяют `~/.codex/AGENTS.md` (или `CODEX_HOME/AGENTS.md`, если путь переопределён) с проектным `./AGENTS.md`, а затем добавляют runtime-overlay.