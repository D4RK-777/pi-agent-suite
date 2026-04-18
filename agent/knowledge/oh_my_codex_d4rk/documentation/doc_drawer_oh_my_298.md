nce: gateway timeout > env override > 5000 default
export OMX_OPENCLAW_COMMAND_TIMEOUT_MS=120000
```

## Prompt tuning guide (concise + context-aware)

For OpenClaw integrations, the most important quality lever is the hook
`instruction` template under:

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

### Recommended context tokens

Always include:

- `{{sessionId}}` for cross-log traceability
- `{{tmuxSession}}` for direct tmux follow-up targeting

Include when relevant: