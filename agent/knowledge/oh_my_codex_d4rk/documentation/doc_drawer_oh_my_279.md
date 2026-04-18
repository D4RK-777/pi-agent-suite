tion`
- `notifications.openclaw.hooks["session-end"].instruction`

## Tokens de contexte recommandés

- Toujours : `{{sessionId}}`, `{{tmuxSession}}`
- Selon l’événement : `{{projectName}}`, `{{question}}`, `{{reason}}`

## Stratégie de verbosité

- `minimal` : signaux très courts
- `session` : contexte opérationnel concis (recommandé)
- `verbose` : plus de contexte état/action/risque

## Commande de mise à jour rapide (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"