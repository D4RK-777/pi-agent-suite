s\",\"to\":\"completed\",\"claim_token\":\"$CLAIM_TOKEN\"}" --json
```

### 7.2 Mailbox/message flow

```bash
omx team api send-message --input '{"team_name":"e2e-team-demo","from_worker":"leader-fixed","to_worker":"worker-1","body":"ACK: worker-1 ready"}' --json
omx team api broadcast --input '{"team_name":"e2e-team-demo","from_worker":"leader-fixed","body":"Sync checkpoint"}' --json
MAILBOX_JSON=$(omx team api mailbox-list --input '{"team_name":"e2e-team-demo","worker":"worker-1"}' --json)
MESSAGE_ID=$(echo "$MAILBOX_JSON" | jq -r '.data.messages[0].message_id // empty')
omx team api mailbox-mark-notified --input "{\"team_name\":\"e2e-team-demo\",\"worker\":\"worker-1\",\"message_id\":\"$MESSAGE_ID\"}" --json