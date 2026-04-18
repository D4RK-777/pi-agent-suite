```

Expected pass signal: JSON includes `"ok":true`.

### B) Delivery verification (`/hooks/agent`)

```bash
curl -sS -o /tmp/omx-openclaw-agent-check.json -w "HTTP %{http_code}\n" \
  -X POST http://127.0.0.1:18789/hooks/agent \
  -H "Authorization: Bearer ${HOOKS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"message":"OMX delivery verification","instruction":"OMX delivery verification","event":"session-end","sessionId":"manual-check"}'
```

Expected pass signal: HTTP 2xx + accepted response body.

## Preflight checks

```bash
# token present
test -n "$HOOKS_TOKEN" && echo "token ok" || echo "token missing"

# reachability
curl -sS -o /dev/null -w "HTTP %{http_code}\n" http://127.0.0.1:18789 || echo "gateway unreachable"