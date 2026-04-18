tus_line`
- `AGENTS.md` theo phạm vi
- Thư mục `.omx/` runtime và cấu hình HUD

## Tác nhân và skill

- Prompt: `prompts/*.md` (cài vào `~/.codex/prompts/` cho `user`, `./.codex/prompts/` cho `project`)
- Skill: `skills/*/SKILL.md` (cài vào `~/.codex/skills/` cho `user`, `./.codex/skills/` cho `project`)

Ví dụ:
- Tác nhân: `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- Skill: `deep-interview`, `ralplan`, `team`, `ralph`, `plan`, `cancel`

## Cấu trúc dự án

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

## Phát triển