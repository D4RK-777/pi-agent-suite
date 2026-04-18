ine`
- `AGENTS.md` для выбранной области
- Директории `.omx/` и конфигурация HUD

## Агенты и навыки

- Промпты: `prompts/*.md` (устанавливаются в `~/.codex/prompts/` для `user`, `./.codex/prompts/` для `project`)
- Навыки: `skills/*/SKILL.md` (устанавливаются в `~/.codex/skills/` для `user`, `./.codex/skills/` для `project`)

Примеры:
- Агенты: `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- Навыки: `deep-interview`, `ralplan`, `team`, `ralph`, `plan`, `cancel`

## Структура проекта

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

## Разработка