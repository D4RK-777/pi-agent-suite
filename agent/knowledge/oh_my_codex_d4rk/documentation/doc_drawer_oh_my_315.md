_current_path}' | grep "$(basename "$PWD")" || true
```

### 3) SOUL.md + #omc-dev follow-up runbook

When a hook suggests active work or pending user action:

1. Read `SOUL.md` and recent `#omc-dev` context.
2. Follow up in Korean, citing `sessionId` + `tmuxSession`.
3. If action is required, state concrete next step (for example, reply needed, retry needed, or session check needed).
4. If delivery looks broken, inspect logs and retry without swallowed output.

Troubleshooting commands:

```bash
# Inspect structured JSONL logs
tail -n 120 /tmp/omx-openclaw-agent.jsonl | jq -s '.[] | {timestamp: (.timestamp // .time), status: (.status // .error // "ok")}'

# Search for errors in logs
rg '"error"|"failed"|"timeout"' /tmp/omx-openclaw-agent.jsonl | tail -20