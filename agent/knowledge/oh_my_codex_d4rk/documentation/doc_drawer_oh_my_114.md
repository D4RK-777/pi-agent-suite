own handling is no longer a separate public workflow.

Seleção de Worker CLI para workers da equipe:

```bash
OMX_TEAM_WORKER_CLI=auto    # padrão; usa claude quando worker --model contém "claude"
OMX_TEAM_WORKER_CLI=codex   # forçar workers Codex CLI
OMX_TEAM_WORKER_CLI=claude  # forçar workers Claude CLI
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # mix de CLI por worker (comprimento=1 ou quantidade de workers)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # opcional: desativar fallback adaptativo queue->resend
```