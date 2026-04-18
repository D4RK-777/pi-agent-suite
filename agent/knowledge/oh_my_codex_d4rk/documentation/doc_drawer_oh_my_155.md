a özel `AGENTS.md`
- `.omx/` çalışma zamanı dizinleri ve HUD yapılandırması

## Ajanlar ve Skill'ler

- Prompt'lar: `prompts/*.md` (`user` için `~/.codex/prompts/`'a, `project` için `./.codex/prompts/`'a kurulur)
- Skill'ler: `skills/*/SKILL.md` (`user` için `~/.codex/skills/`'a, `project` için `./.codex/skills/`'a kurulur)

Örnekler:
- Ajanlar: `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- Skill'ler: `deep-interview`, `ralplan`, `team`, `ralph`, `plan`, `cancel`

## Proje Yapısı

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

## Geliştirme