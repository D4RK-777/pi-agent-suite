ig` / `--effort` pour que Claude utilise le `settings.json` par défaut.

## Ce que `omx setup` écrit

- `.omx/setup-scope.json` (scope de setup persisté)
- Installations dépendantes du scope :
  - `user` : `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project` : `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Comportement au lancement : si le scope persisté est `project`, le lancement `omx` utilise automatiquement `CODEX_HOME=./.codex` (sauf si `CODEX_HOME` est déjà défini).
- Les instructions de lancement fusionnent `~/.codex/AGENTS.md` (ou `CODEX_HOME/AGENTS.md` s'il est redéfini) avec `./AGENTS.md` du projet, puis ajoutent l'overlay d'exécution.