FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```

### 4b) `custom_cli_command`

Use AskUserQuestion to collect:
- Command template (supports `{{event}}`, `{{instruction}}`, `{{sessionId}}`, `{{projectPath}}`)
- Optional event list
- Optional instruction template

Write:

```bash
jq \
  --arg command "$COMMAND_TEMPLATE" \
  --arg instruction "${INSTRUCTION:-OMX event {{event}} for {{projectPath}}}" \
  '.notifications = (.notifications // {enabled: true}) |
   .notifications.enabled = true |
   .notifications.custom_cli_command = {
     enabled: true,
     command: $command,
     instruction: $instruction,
     events: ["session-end", "ask-user-question"]
   }' "$CONFIG_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```