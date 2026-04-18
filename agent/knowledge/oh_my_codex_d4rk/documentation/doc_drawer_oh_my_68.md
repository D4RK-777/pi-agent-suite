tdown handling is no longer a separate public workflow.

Selezione CLI worker per i worker del team:

```bash
OMX_TEAM_WORKER_CLI=auto    # predefinito; usa claude quando worker --model contiene "claude"
OMX_TEAM_WORKER_CLI=codex   # forza i worker Codex CLI
OMX_TEAM_WORKER_CLI=claude  # forza i worker Claude CLI
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # mix CLI per worker (lunghezza=1 o numero di worker)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # opzionale: disabilita il fallback adattivo queue->resend
```