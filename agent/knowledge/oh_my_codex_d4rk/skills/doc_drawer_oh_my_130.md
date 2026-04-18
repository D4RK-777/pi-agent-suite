own, profiles, reply listener
7. **Disable all notifications** - set `notifications.enabled = false`

## Step 3: Configure Native Platforms (Discord / Telegram / Slack)

Collect and validate platform-specific values, then write directly under native keys:

- Discord webhook: `notifications.discord`
- Discord bot: `notifications["discord-bot"]`
- Telegram: `notifications.telegram`
- Slack: `notifications.slack`

Do not write these as generic command/webhook aliases.

## Step 4: Configure Generic Extensibility

### 4a) `custom_webhook_command`

Use AskUserQuestion to collect:
- URL
- Optional headers
- Optional method (`POST` default, or `PUT`)
- Optional event list (`session-end`, `ask-user-question`, `session-start`, `session-idle`, `stop`)
- Optional instruction template

Write: