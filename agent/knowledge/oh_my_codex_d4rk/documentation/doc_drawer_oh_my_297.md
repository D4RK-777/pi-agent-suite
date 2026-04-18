# OpenClaw / Generic Notification Gateway Integration Guide

This guide covers two supported setup paths:

1. **Explicit OpenClaw schema** (`notifications.openclaw`) — runtime-native shape
2. **Generic aliases** (`custom_webhook_command`, `custom_cli_command`) — flexible setup for OpenClaw or other services

## Activation gates

```bash
# Prefer exporting a token env var in your shell profile (avoid hardcoding secrets in JSON):
export HOOKS_TOKEN="your-openclaw-hooks-token"

# Required for OpenClaw dispatch pipeline
export OMX_OPENCLAW=1

# Required in addition for command gateways
export OMX_OPENCLAW_COMMAND=1

# Optional global default for command gateway timeout (ms)
# Precedence: gateway timeout > env override > 5000 default
export OMX_OPENCLAW_COMMAND_TIMEOUT_MS=120000
```