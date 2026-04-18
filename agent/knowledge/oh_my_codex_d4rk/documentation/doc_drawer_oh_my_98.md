(추가 시작 인수 없음) 명시적인 `--model` / `--config` / `--effort` 재정의를 무시하여 Claude가 기본 `settings.json`을 사용합니다.

## `omx setup`이 작성하는 것

- `.omx/setup-scope.json` (저장된 설정 범위)
- 범위에 따른 설치:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- 시작 동작: 저장된 범위가 `project`이면, `omx` 시작 시 자동으로 `CODEX_HOME=./.codex`를 사용합니다 (`CODEX_HOME`이 이미 설정되지 않은 경우).
- 시작 지침은 `~/.codex/AGENTS.md`(또는 `CODEX_HOME/AGENTS.md`)와 프로젝트 `./AGENTS.md`를 병합한 뒤 런타임 오버레이를 추가해 사용합니다.
- 기존 `AGENTS.md`는 자동으로 덮어쓰지 않습니다. 대화형 TTY 실행에서는 덮어쓸지 확인하고, 비대화형 실행에서는 `--force`가 없으면 건너뜁니다 (활성 세션 안전 검사는 여전히 적용됩니다).
- `config.toml` 업데이트 (두 범위 모두):
  - `notify = ["node", "..."]`