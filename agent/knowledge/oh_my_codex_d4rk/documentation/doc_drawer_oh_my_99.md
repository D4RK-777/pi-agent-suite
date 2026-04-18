가 없으면 건너뜁니다 (활성 세션 안전 검사는 여전히 적용됩니다).
- `config.toml` 업데이트 (두 범위 모두):
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - MCP 서버 항목 (`omx_state`, `omx_memory`, `omx_code_intel`, `omx_trace`)
  - `[tui] status_line`
- 범위별 `AGENTS.md`
- `.omx/` 런타임 디렉토리 및 HUD 설정

## 에이전트와 스킬

- 프롬프트: `prompts/*.md` (`user`는 `~/.codex/prompts/`에, `project`는 `./.codex/prompts/`에 설치)
- 스킬: `skills/*/SKILL.md` (`user`는 `~/.codex/skills/`에, `project`는 `./.codex/skills/`에 설치)

예시:
- 에이전트: `architect`, `planner`, `executor`, `debugger`, `verifier`, `security-reviewer`
- 스킬: `deep-interview`, `ralplan`, `team`, `ralph`, `plan`, `cancel`

## 프로젝트 구조