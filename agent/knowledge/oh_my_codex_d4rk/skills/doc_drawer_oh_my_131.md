ask-user-question`, `session-start`, `session-idle`, `stop`)
- Optional instruction template

Write:

```bash
jq \
  --arg url "$URL" \
  --arg method "${METHOD:-POST}" \
  --arg instruction "${INSTRUCTION:-OMX event {{event}} for {{projectPath}}}" \
  '.notifications = (.notifications // {enabled: true}) |
   .notifications.enabled = true |
   .notifications.custom_webhook_command = {
     enabled: true,
     url: $url,
     method: $method,
     instruction: $instruction,
     events: ["session-end", "ask-user-question"]
   }' "$CONFIG_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```

### 4b) `custom_cli_command`