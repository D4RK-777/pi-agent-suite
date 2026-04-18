are removed.

## Step 1: Inspect Current State

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"

if [ -f "$CONFIG_FILE" ]; then
  jq -r '
    {
      notifications_enabled: (.notifications.enabled // false),
      discord: (.notifications.discord.enabled // false),
      discord_bot: (.notifications["discord-bot"].enabled // false),
      telegram: (.notifications.telegram.enabled // false),
      slack: (.notifications.slack.enabled // false),
      openclaw: (.notifications.openclaw.enabled // false),
      custom_webhook_command: (.notifications.custom_webhook_command.enabled // false),
      custom_cli_command: (.notifications.custom_cli_command.enabled // false),
      verbosity: (.notifications.verbosity // "session"),