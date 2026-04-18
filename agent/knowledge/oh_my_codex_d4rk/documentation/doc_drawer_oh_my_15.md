spezifische `AGENTS.md`
- `.omx/`-Laufzeitverzeichnisse und HUD-Konfiguration

## Agenten und Skills

- Prompts: `prompts/*.md` (installiert nach `~/.codex/prompts/` für `user`, `./.codex/prompts/` für `project`)
- Skills: `skills/*/SKILL.md` (installiert nach `~/.codex/skills/` für `user`, `./.codex/skills/` für `project`)

Beispiele:
- Agenten: `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- Skills: `deep-interview`, `ralplan`, `team`, `ralph`, `plan`, `cancel`

## Projektstruktur

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

## Entwicklung