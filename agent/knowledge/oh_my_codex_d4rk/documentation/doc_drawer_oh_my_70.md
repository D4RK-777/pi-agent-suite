fig` / `--effort` in modo che Claude usi il `settings.json` predefinito.

## Cosa scrive `omx setup`

- `.omx/setup-scope.json` (scope di setup persistito)
- Installazioni dipendenti dallo scope:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Comportamento all'avvio: se lo scope persistito è `project`, l'avvio `omx` usa automaticamente `CODEX_HOME=./.codex` (a meno che `CODEX_HOME` non sia già impostato).
- Le istruzioni di avvio uniscono `~/.codex/AGENTS.md` (o `CODEX_HOME/AGENTS.md` se ridefinito) con `./AGENTS.md` del progetto, quindi aggiungono l'overlay di runtime.