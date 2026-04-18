me":"e2e-team-demo","task_id":"<TASK_ID>","claim_token":"<CLAIM_TOKEN>","worker":"worker-1"}' --json
omx team api read-config --input '{"team_name":"e2e-team-demo"}' --json
omx team api read-manifest --input '{"team_name":"e2e-team-demo"}' --json
omx team api read-worker-status --input '{"team_name":"e2e-team-demo","worker":"worker-1"}' --json
omx team api read-worker-heartbeat --input '{"team_name":"e2e-team-demo","worker":"worker-1"}' --json
omx team api update-worker-heartbeat --input '{"team_name":"e2e-team-demo","worker":"worker-1","pid":12345,"turn_count":12,"alive":true}' --json
omx team api write-worker-inbox --input '{"team_name":"e2e-team-demo","worker":"worker-1","content":"# Inbox update\nProceed with task 2."}' --json