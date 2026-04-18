aliases)

For Korean-first tmux follow-up operations in `#omc-dev`, see the dev guide section below.

```json
{
  "notifications": {
    "enabled": true,
    "verbosity": "verbose",
    "events": {
      "session-start": { "enabled": true },
      "session-idle": { "enabled": true },
      "ask-user-question": { "enabled": true },
      "session-stop": { "enabled": true },
      "session-end": { "enabled": true }
    },
    "openclaw": {
      "enabled": true,
      "gateways": {
        "local": {
          "type": "command",
          "command": "(clawdbot agent --session-id omx-hooks --message {{instruction}} --thinking minimal --deliver --reply-channel discord --reply-to 'channel:1468539002985644084' --timeout 120 --json >>/tmp/omx-openclaw-agent.jsonl 2>&1 || true)",