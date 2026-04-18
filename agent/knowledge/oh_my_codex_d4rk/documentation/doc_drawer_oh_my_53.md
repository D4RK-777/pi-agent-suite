tatus_line`
- `AGENTS.md` spécifique au scope
- Répertoires d'exécution `.omx/` et configuration HUD

## Agents et Skills

- Prompts : `prompts/*.md` (installés dans `~/.codex/prompts/` pour `user`, `./.codex/prompts/` pour `project`)
- Skills : `skills/*/SKILL.md` (installés dans `~/.codex/skills/` pour `user`, `./.codex/skills/` pour `project`)

Exemples :
- Agents : `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- Skills : `autopilot`, `plan`, `team`, `ralph`, `ultrawork`, `cancel`

## Structure du projet

```text
oh-my-codex/
  bin/omx.js
  src/
    cli/
    team/
    mcp/
    hooks/
    hud/
    config/
    modes/
    notifications/
    verification/
  prompts/
  skills/
  templates/
  scripts/
```

## Développement