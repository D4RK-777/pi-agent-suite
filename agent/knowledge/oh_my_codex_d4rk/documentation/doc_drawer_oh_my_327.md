on`
- `notifications.openclaw.hooks["session-end"].instruction`

## Рекомендуемые контекстные токены

- Всегда включать: `{{sessionId}}`, `{{tmuxSession}}`
- По событию: `{{projectName}}`, `{{question}}`, `{{reason}}`

## Стратегия детализации (verbosity)

- `minimal`: очень короткие уведомления
- `session`: сжатый операционный контекст (рекомендуется)
- `verbose`: расширенный контекст статуса/действий/рисков

## Быстрая команда обновления (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"