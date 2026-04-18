ration.de.md) | [Français](./openclaw-integration.fr.md) | [Italiano](./openclaw-integration.it.md)


Diese Seite lokalisiert den Abschnitt **„Prompt tuning guide (concise + context-aware)”** aus der englischen Hauptdokumentation.

Für die vollständige Integrationsdokumentation (Gateways, Hooks, Verifikation) siehe [English guide](./openclaw-integration.md).

## Prompt-Optimierung (prägnant + kontextbewusst)

## Wo Prompt-Vorlagen bearbeitet werden

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Empfohlene Kontext-Token