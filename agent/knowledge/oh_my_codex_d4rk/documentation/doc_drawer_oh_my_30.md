dling is no longer a separate public workflow.

Selección de Worker CLI para los workers del equipo:

```bash
OMX_TEAM_WORKER_CLI=auto    # predeterminado; usa claude cuando worker --model contiene "claude"
OMX_TEAM_WORKER_CLI=codex   # forzar workers Codex CLI
OMX_TEAM_WORKER_CLI=claude  # forzar workers Claude CLI
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # mezcla de CLI por worker (longitud=1 o cantidad de workers)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # opcional: desactivar fallback adaptativo queue->resend
```