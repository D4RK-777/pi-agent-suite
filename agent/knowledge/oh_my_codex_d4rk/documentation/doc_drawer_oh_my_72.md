tus_line`
- `AGENTS.md` specifico dello scope
- Directory di esecuzione `.omx/` e configurazione HUD

## Agenti e Skill

- Prompt: `prompts/*.md` (installati in `~/.codex/prompts/` per `user`, `./.codex/prompts/` per `project`)
- Skill: `skills/*/SKILL.md` (installati in `~/.codex/skills/` per `user`, `./.codex/skills/` per `project`)

Esempi:
- Agenti: `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- Skill: `deep-interview`, `ralplan`, `team`, `ralph`, `plan`, `cancel`

## Struttura del progetto

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

## Sviluppo