을 병렬로 조율해 실행하려면 `$team`, 한 명의 책임자가 끝까지 밀고 검증하려면 `$ralph`를 사용합니다.

## 핵심 모델

OMX는 다음 레이어를 설치하고 연결합니다:

```text
User
  -> Codex CLI
    -> AGENTS.md (오케스트레이션 브레인)
    -> ~/.codex/prompts/*.md (에이전트 프롬프트 카탈로그)
    -> ~/.codex/skills/*/SKILL.md (스킬 카탈로그)
    -> ~/.codex/config.toml (기능, 알림, MCP)
    -> .omx/ (런타임 상태, 메모리, 계획, 로그)
```

## 주요 명령어

```bash
omx                # Codex 실행 (tmux에서 HUD와 함께)
omx setup          # 범위별 프롬프트/스킬/설정 설치 + 프로젝트 .omx + 범위별 AGENTS.md
omx doctor         # 설치/런타임 진단
omx doctor --team  # Team/swarm 진단
omx team ...       # tmux 팀 워커 시작/상태/재개/종료
omx status         # 활성 모드 표시
omx cancel         # 활성 실행 모드 취소
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (플러그인 확장 워크플로우)