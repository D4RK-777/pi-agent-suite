line`
- `AGENTS.md` específico del alcance
- Directorios `.omx/` de ejecución y configuración de HUD

## Agentes y skills

- Prompts: `prompts/*.md` (instalados en `~/.codex/prompts/` para `user`, `./.codex/prompts/` para `project`)
- Skills: `skills/*/SKILL.md` (instalados en `~/.codex/skills/` para `user`, `./.codex/skills/` para `project`)

Ejemplos:
- Agentes: `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- Skills: `deep-interview`, `ralplan`, `team`, `ralph`, `plan`, `cancel`

## Estructura del proyecto

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

## Desarrollo