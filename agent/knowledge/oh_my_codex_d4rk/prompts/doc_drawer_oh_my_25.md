erop (`omx team api ... --json`) with the stable JSON envelope.

### 7.1 Task lifecycle (claim-safe)

```bash
CREATE_JSON=$(omx team api create-task --input '{"team_name":"e2e-team-demo","subject":"Demo lifecycle","description":"Claim-safe lifecycle demo","owner":"worker-1"}' --json)
TASK_ID=$(echo "$CREATE_JSON" | jq -r '.data.task.id')

CLAIM_JSON=$(omx team api claim-task --input "{\"team_name\":\"e2e-team-demo\",\"task_id\":\"$TASK_ID\",\"worker\":\"worker-1\",\"expected_version\":1}" --json)
CLAIM_TOKEN=$(echo "$CLAIM_JSON" | jq -r '.data.claimToken')

omx team api transition-task-status --input "{\"team_name\":\"e2e-team-demo\",\"task_id\":\"$TASK_ID\",\"from\":\"in_progress\",\"to\":\"completed\",\"claim_token\":\"$CLAIM_TOKEN\"}" --json
```

### 7.2 Mailbox/message flow