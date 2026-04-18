`--config` / `--effort` para que o Claude use o `settings.json` padrão.

## O que `omx setup` grava

- `.omx/setup-scope.json` (escopo de instalação persistido)
- Instalações dependentes do escopo:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Comportamento de inicialização: se o escopo persistido for `project`, o lançamento do `omx` usa automaticamente `CODEX_HOME=./.codex` (a menos que `CODEX_HOME` já esteja definido).
- As instruções de inicialização combinam `~/.codex/AGENTS.md` (ou `CODEX_HOME/AGENTS.md`, quando sobrescrito) com o `./AGENTS.md` do projeto e depois adicionam o overlay de runtime.