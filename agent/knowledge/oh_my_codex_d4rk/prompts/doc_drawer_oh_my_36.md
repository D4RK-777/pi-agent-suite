ker-1\"}" --json)
MESSAGE_ID=$(echo "$MAILBOX_JSON" | jq -r '.data.messages[0].message_id // empty')
omx team api mailbox-mark-notified --input "{\"team_name\":\"$TEAM_NAME\",\"worker\":\"worker-1\",\"message_id\":\"$MESSAGE_ID\"}" --json
omx team api mailbox-mark-delivered --input "{\"team_name\":\"$TEAM_NAME\",\"worker\":\"worker-1\",\"message_id\":\"$MESSAGE_ID\"}" --json

echo "[7/8] summary envelope check"
omx team api get-summary --input "{\"team_name\":\"$TEAM_NAME\"}" --json | jq -e '.schema_version == "1.0" and .operation == "get-summary" and .ok == true'

echo "[8/8] shutdown + cleanup"
omx team shutdown "$TEAM_NAME"
omx team api cleanup --input "{\"team_name\":\"$TEAM_NAME\"}" --json

echo "E2E demo complete."
```