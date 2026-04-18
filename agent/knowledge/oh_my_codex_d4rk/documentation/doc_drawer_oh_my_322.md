ion`
- `notifications.openclaw.hooks["session-end"].instruction`

## Tokens de contexto recomendados

- Sempre incluir: `{{sessionId}}`, `{{tmuxSession}}`
- Conforme evento: `{{projectName}}`, `{{question}}`, `{{reason}}`

## Estratégia de verbosidade

- `minimal`: avisos muito curtos
- `session`: contexto operacional conciso (recomendado)
- `verbose`: mais contexto de status/ação/risco

## Comando rápido de atualização (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"