stic and backward compatible.

## Option A: Explicit `notifications.openclaw` (legacy/runtime shape)

```json
{
  "notifications": {
    "enabled": true,
    "openclaw": {
      "enabled": true,
      "gateways": {
        "local": {
          "type": "http",
          "url": "http://127.0.0.1:18789/hooks/agent",
          "headers": {
            "Authorization": "Bearer ${HOOKS_TOKEN}"
          }
        }
      },
      "hooks": {
        "session-end": {
          "enabled": true,
          "gateway": "local",
          "instruction": "OMX task completed for {{projectPath}}"
        },
        "ask-user-question": {
          "enabled": true,
          "gateway": "local",
          "instruction": "OMX needs input: {{question}}"
        }
      }
    }
  }
}
```