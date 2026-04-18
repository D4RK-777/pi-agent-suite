curl -sS -o /dev/null -w "HTTP %{http_code}\n" http://127.0.0.1:18789 || echo "gateway unreachable"

# gate checks
test "$OMX_OPENCLAW" = "1" && echo "OMX_OPENCLAW=1" || echo "missing OMX_OPENCLAW=1"
test "$OMX_OPENCLAW_COMMAND" = "1" && echo "OMX_OPENCLAW_COMMAND=1" || echo "missing OMX_OPENCLAW_COMMAND=1"
```

## Pass/Fail Diagnostics

- **401/403**: invalid/missing bearer token.
- **404**: wrong path; verify `/hooks/agent` and `/hooks/wake`.
- **5xx**: gateway runtime issue; inspect logs.
- **Timeout/connection refused**: host/port/firewall issue.
- **Command gateway disabled**: set both `OMX_OPENCLAW=1` and `OMX_OPENCLAW_COMMAND=1`.
- **Command killed by `SIGTERM`**: increase `gateways.<name>.timeout` (recommend `120000` for clawdbot agent) or set `OMX_OPENCLAW_COMMAND_TIMEOUT_MS`.