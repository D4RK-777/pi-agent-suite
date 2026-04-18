alph shutdown handling is no longer a separate public workflow.

Worker-CLI-Auswahl für Team-Worker:

```bash
OMX_TEAM_WORKER_CLI=auto    # Standard; verwendet claude wenn Worker --model "claude" enthält
OMX_TEAM_WORKER_CLI=codex   # Codex-CLI-Worker erzwingen
OMX_TEAM_WORKER_CLI=claude  # Claude-CLI-Worker erzwingen
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # CLI-Mix pro Worker (Länge=1 oder Worker-Anzahl)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # optional: adaptiven Queue->Resend-Fallback deaktivieren
```