ndling is no longer a separate public workflow.

Sélection du CLI worker pour les workers d'équipe :

```bash
OMX_TEAM_WORKER_CLI=auto    # par défaut ; utilise claude quand worker --model contient "claude"
OMX_TEAM_WORKER_CLI=codex   # forcer les workers Codex CLI
OMX_TEAM_WORKER_CLI=claude  # forcer les workers Claude CLI
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # mix CLI par worker (longueur=1 ou nombre de workers)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # optionnel : désactiver le fallback adaptatif queue->resend
```