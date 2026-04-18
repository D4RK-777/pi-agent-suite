nstruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Empfohlene Kontext-Token

- Immer: `{{sessionId}}`, `{{tmuxSession}}`
- Ereignisabhängig: `{{projectName}}`, `{{question}}`, `{{reason}}`

## Ausführlichkeitsstrategie

- `minimal`: sehr kurze Signale
- `session`: kompakter Betriebs-Kontext (empfohlen)
- `verbose`: mehr Status-, Aktions- und Risikokontext

## Schnellupdate-Befehl (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"