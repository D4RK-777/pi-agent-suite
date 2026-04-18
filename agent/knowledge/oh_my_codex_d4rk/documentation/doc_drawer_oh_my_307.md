"local",
          "instruction": "OMX needs input: {{question}}"
        }
      }
    }
  }
}
```

## Option B: Generic aliases (`custom_webhook_command` / `custom_cli_command`)

```json
{
  "notifications": {
    "enabled": true,
    "custom_webhook_command": {
      "enabled": true,
      "url": "http://127.0.0.1:18789/hooks/agent",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer ${HOOKS_TOKEN}"
      },
      "events": ["session-end", "ask-user-question"],
      "instruction": "OMX event {{event}} for {{projectPath}}"
    },
    "custom_cli_command": {
      "enabled": true,
      "command": "~/.local/bin/my-notifier --event {{event}} --text {{instruction}}",
      "events": ["session-end"],
      "instruction": "OMX event {{event}} for {{projectPath}}"