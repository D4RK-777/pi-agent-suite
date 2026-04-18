laude)"
omx team 6:executor "$TEAM_TASK"

echo "[2/8] lifecycle status"
omx team status "$TEAM_NAME"

echo "[3/8] create task"
CREATE_JSON=$(omx team api create-task --input "{\"team_name\":\"$TEAM_NAME\",\"subject\":\"one-shot lifecycle\",\"description\":\"demo task\",\"owner\":\"worker-1\"}" --json)
TASK_ID=$(echo "$CREATE_JSON" | jq -r '.data.task.id')

echo "[4/8] claim task"
CLAIM_JSON=$(omx team api claim-task --input "{\"team_name\":\"$TEAM_NAME\",\"task_id\":\"$TASK_ID\",\"worker\":\"worker-1\",\"expected_version\":1}" --json)
CLAIM_TOKEN=$(echo "$CLAIM_JSON" | jq -r '.data.claimToken')