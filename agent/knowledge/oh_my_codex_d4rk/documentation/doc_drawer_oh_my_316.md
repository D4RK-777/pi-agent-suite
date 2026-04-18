# Search for errors in logs
rg '"error"|"failed"|"timeout"' /tmp/omx-openclaw-agent.jsonl | tail -20

# Manual retry with production-tested settings
clawdbot agent --session-id omx-hooks \
  --message "OMX hook retry 점검: session={{sessionId}} tmux={{tmuxSession}}" \
  --thinking minimal --deliver --reply-channel discord --reply-to 'channel:1468539002985644084' \
  --timeout 120 --json
```

## Verification (required)

### A) Wake smoke test (`/hooks/wake`)

```bash
curl -sS -X POST http://127.0.0.1:18789/hooks/wake \
  -H "Authorization: Bearer ${HOOKS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"text":"OMX wake smoke test","mode":"now"}'
```

Expected pass signal: JSON includes `"ok":true`.

### B) Delivery verification (`/hooks/agent`)