ration.de.md) | [Français](./openclaw-integration.fr.md) | [Italiano](./openclaw-integration.it.md)


Cette page localise la section **« Prompt tuning guide (concise + context-aware) »** de la documentation principale en anglais.

Pour la documentation complète d’intégration (gateways, hooks, vérification), voir le [English guide](./openclaw-integration.md).

## Réglage des prompts (concis et contextuel)

## Où modifier les modèles de prompt

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Tokens de contexte recommandés