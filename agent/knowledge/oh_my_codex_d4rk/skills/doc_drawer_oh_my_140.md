_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```

Verification for this mode:

```bash
clawdbot agent --session-id omx-hooks --message "OMX hook test via clawdbot agent path" \
  --thinking minimal --deliver --reply-channel discord --reply-to 'channel:1468539002985644084' --timeout 120 --json
```

Dev runbook (Korean + tmux follow-up):

```bash
# 1) identify active OMX tmux sessions
tmux list-sessions -F '#{session_name}' | rg '^omx-' || true

# 2) confirm hook templates include session/tmux context
jq '.notifications.openclaw.hooks' "$CONFIG_FILE"

# 3) inspect agent JSONL logs when delivery looks broken
tail -n 120 /tmp/omx-openclaw-agent.jsonl | jq -s '.[] | {timestamp: (.timestamp // .time), status: (.status // .error // "ok")}'