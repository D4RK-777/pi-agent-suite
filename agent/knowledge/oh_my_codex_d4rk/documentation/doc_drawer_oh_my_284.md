ction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Token di contesto consigliati

- Sempre: `{{sessionId}}`, `{{tmuxSession}}`
- Per evento: `{{projectName}}`, `{{question}}`, `{{reason}}`

## Strategia di verbosità

- `minimal`: avvisi molto brevi
- `session`: contesto operativo conciso (consigliato)
- `verbose`: più contesto su stato/azione/rischio

## Comando rapido di aggiornamento (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"