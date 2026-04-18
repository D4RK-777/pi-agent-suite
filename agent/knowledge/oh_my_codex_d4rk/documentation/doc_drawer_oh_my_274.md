ion`
- `notifications.openclaw.hooks["session-end"].instruction`

## Tokens de contexto recomendados

- Siempre: `{{sessionId}}`, `{{tmuxSession}}`
- Según evento: `{{projectName}}`, `{{question}}`, `{{reason}}`

## Estrategia de verbosidad

- `minimal`: avisos muy cortos
- `session`: contexto operativo conciso (recomendado)
- `verbose`: más contexto de estado, acción y riesgo

## Comando rápido de actualización (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"