ration.de.md) | [Français](./openclaw-integration.fr.md) | [Italiano](./openclaw-integration.it.md)


Эта страница локализует раздел **“Prompt tuning guide (concise + context-aware)”** из основной англоязычной документации.

Полное руководство по интеграции (gateway, hooks, проверка) см. в [English guide](./openclaw-integration.md).

## Тюнинг промптов (кратко + с учетом контекста)

## Где редактировать шаблоны промптов

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Рекомендуемые контекстные токены