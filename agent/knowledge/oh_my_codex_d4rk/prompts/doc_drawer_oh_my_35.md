er-1\",\"expected_version\":1}" --json)
CLAIM_TOKEN=$(echo "$CLAIM_JSON" | jq -r '.data.claimToken')

echo "[5/8] transition task -> completed"
omx team api transition-task-status --input "{\"team_name\":\"$TEAM_NAME\",\"task_id\":\"$TASK_ID\",\"from\":\"in_progress\",\"to\":\"completed\",\"claim_token\":\"$CLAIM_TOKEN\"}" --json

echo "[6/8] mailbox flow"
omx team api send-message --input "{\"team_name\":\"$TEAM_NAME\",\"from_worker\":\"leader-fixed\",\"to_worker\":\"worker-1\",\"body\":\"ACK one-shot\"}" --json
MAILBOX_JSON=$(omx team api mailbox-list --input "{\"team_name\":\"$TEAM_NAME\",\"worker\":\"worker-1\"}" --json)
MESSAGE_ID=$(echo "$MAILBOX_JSON" | jq -r '.data.messages[0].message_id // empty')