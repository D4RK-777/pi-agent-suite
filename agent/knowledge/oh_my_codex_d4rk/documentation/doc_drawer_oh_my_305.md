다음: 후속 액션 1~2개"' \
  "$CONFIG_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```

## Canonical precedence contract

When both explicit OpenClaw config and generic aliases are present:

1. `notifications.openclaw` wins
2. `custom_webhook_command` / `custom_cli_command` are ignored
3. OMX emits a warning for clarity

This keeps behavior deterministic and backward compatible.

## Option A: Explicit `notifications.openclaw` (legacy/runtime shape)