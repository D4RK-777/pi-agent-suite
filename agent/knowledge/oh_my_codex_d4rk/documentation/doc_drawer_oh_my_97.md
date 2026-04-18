acy linked-Ralph shutdown handling is no longer a separate public workflow.

팀 워커를 위한 Worker CLI 선택:

```bash
OMX_TEAM_WORKER_CLI=auto    # 기본값; worker --model에 "claude"가 포함되면 claude 사용
OMX_TEAM_WORKER_CLI=codex   # Codex CLI 워커 강제
OMX_TEAM_WORKER_CLI=claude  # Claude CLI 워커 강제
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # 워커별 CLI 혼합 (길이=1 또는 워커 수)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # 선택: 적응형 queue->resend 폴백 비활성화
```

참고:
- 워커 시작 인수는 여전히 `OMX_TEAM_WORKER_LAUNCH_ARGS`를 통해 공유됩니다.
- `OMX_TEAM_WORKER_CLI_MAP`은 워커별 선택을 위해 `OMX_TEAM_WORKER_CLI`를 재정의합니다.
- 트리거 제출은 기본적으로 적응형 재시도를 사용합니다 (queue/submit, 필요시 안전한 clear-line+resend 폴백).
- Claude worker 모드에서 OMX는 워커를 일반 `claude`로 시작하고 (추가 시작 인수 없음) 명시적인 `--model` / `--config` / `--effort` 재정의를 무시하여 Claude가 기본 `settings.json`을 사용합니다.