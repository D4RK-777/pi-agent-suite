ph shutdown handling is no longer a separate public workflow.

Выбор Worker CLI для рабочих команды:

```bash
OMX_TEAM_WORKER_CLI=auto    # по умолчанию; использует claude, если worker --model содержит "claude"
OMX_TEAM_WORKER_CLI=codex   # принудительно Codex CLI
OMX_TEAM_WORKER_CLI=claude  # принудительно Claude CLI
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # CLI для каждого рабочего (длина=1 или количество рабочих)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # опционально: отключить адаптивный откат queue->resend
```