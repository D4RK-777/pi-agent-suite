ut "{\"team_name\":\"e2e-team-demo\",\"worker\":\"worker-1\",\"message_id\":\"$MESSAGE_ID\"}" --json
omx team api mailbox-mark-delivered --input "{\"team_name\":\"e2e-team-demo\",\"worker\":\"worker-1\",\"message_id\":\"$MESSAGE_ID\"}" --json
```

### 7.3 Complete operations matrix (broad coverage)

```bash
omx team api read-task --input '{"team_name":"e2e-team-demo","task_id":"<TASK_ID>"}' --json
omx team api list-tasks --input '{"team_name":"e2e-team-demo"}' --json
omx team api update-task --input '{"team_name":"e2e-team-demo","task_id":"<TASK_ID>","description":"Updated via CLI interop"}' --json
omx team api release-task-claim --input '{"team_name":"e2e-team-demo","task_id":"<TASK_ID>","claim_token":"<CLAIM_TOKEN>","worker":"worker-1"}' --json