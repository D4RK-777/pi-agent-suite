lse)'

# Team lifecycle checks
omx team status "e2e-team-demo"
omx team shutdown "e2e-team-demo"
```

Success criteria:
- All `omx team api` examples return valid JSON envelopes.
- Task lifecycle uses `create-task -> claim-task -> transition-task-status`.
- Message lifecycle uses `send-message/broadcast -> mailbox-list -> mailbox-mark-*`.
- Team lifecycle demonstrates `omx team`, `omx team status`, `omx team resume`, and `omx team shutdown`.

## Demo 8: One-Shot E2E Script (Copy/Paste)

Use the bundled helper script:

```bash
chmod +x scripts/demo-team-e2e.sh
./scripts/demo-team-e2e.sh
```

Optional overrides:

```bash
TEAM_TASK="e2e team demo" \
TEAM_NAME="e2e-team-demo" \
WORKER_COUNT=6 \
OMX_TEAM_WORKER_LAUNCH_MODE=prompt \
./scripts/demo-team-e2e.sh
```