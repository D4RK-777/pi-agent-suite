ehavior, **message/task delivery must not be driven by ad-hoc tmux typing**.

Required default path:

1. Use `omx team ...` runtime lifecycle commands for orchestration.
2. Use `omx team api ... --json` for mailbox/task mutations.
3. Verify delivery via mailbox/state evidence (`mailbox/*.json`, task status, `omx team status`).

Strict rules:

- **MUST NOT** use direct `tmux send-keys` as the primary mechanism to deliver instructions/messages.
- **MUST NOT** spam Enter/trigger keys without first checking runtime/state evidence.
- **MUST** prefer durable state writes + runtime dispatch (`dispatch/requests.json`, mailbox, inbox).