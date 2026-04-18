ration.de.md) | [Français](./openclaw-integration.fr.md) | [Italiano](./openclaw-integration.it.md)


Questa pagina localizza la sezione **“Prompt tuning guide (concise + context-aware)”** della documentazione principale in inglese.

Per la guida completa di integrazione (gateway, hook, verifica), vedi [English guide](./openclaw-integration.md).

## Tuning prompt (conciso e context-aware)

## Dove modificare i template dei prompt

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Token di contesto consigliati