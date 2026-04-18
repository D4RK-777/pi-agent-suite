y (preferred over channel aliases).

Example (targeting `#omc-dev` with production-tested settings):

```bash
jq \
  --arg command "(clawdbot agent --session-id omx-hooks --message {{instruction}} --thinking minimal --deliver --reply-channel discord --reply-to 'channel:1468539002985644084' --timeout 120 --json >>/tmp/omx-openclaw-agent.jsonl 2>&1 || true)" \
  '.notifications = (.notifications // {enabled: true}) |
   .notifications.enabled = true |
   .notifications.verbosity = "verbose" |
   .notifications.events = (.notifications.events // {}) |
   .notifications.events["session-start"] = {enabled: true} |
   .notifications.events["session-idle"] = {enabled: true} |
   .notifications.events["ask-user-question"] = {enabled: true} |