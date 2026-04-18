NSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## 팀 모드

병렬 워커가 유리한 대규모 작업에 팀 모드를 사용합니다.

라이프사이클:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

운영 명령어:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

중요 규칙: 중단하는 경우가 아니라면 작업이 `in_progress` 상태인 동안 종료하지 마세요.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

팀 워커를 위한 Worker CLI 선택: