-agent.jsonl | jq -s '.[] | {timestamp: (.timestamp // .time), status: (.status // .error // "ok")}'

# 4) check for recent errors in logs
rg '"error"|"failed"|"timeout"' /tmp/omx-openclaw-agent.jsonl | tail -20
```

### 4c) Compatibility + precedence contract

OMX accepts both:
- explicit `notifications.openclaw` schema (legacy/runtime shape)
- generic aliases (`custom_webhook_command`, `custom_cli_command`)

Deterministic precedence:
1. `notifications.openclaw` **wins** when present and valid.
2. Generic aliases are ignored in that case (with warning).

## Step 5: Cross-Cutting Settings

### Verbosity
- minimal / session (recommended) / agent / verbose

### Idle cooldown
- `notifications.idleCooldownSeconds`

### Profiles
- `notifications.profiles`
- `notifications.defaultProfile`