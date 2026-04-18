_name":"e2e-team-demo","worker":"worker-1","content":"# Inbox update\nProceed with task 2."}' --json
omx team api write-worker-identity --input '{"team_name":"e2e-team-demo","worker":"worker-9","index":9,"role":"executor"}' --json
omx team api append-event --input '{"team_name":"e2e-team-demo","type":"task_completed","worker":"worker-1","task_id":"<TASK_ID>","reason":"demo"}' --json
omx team api get-summary --input '{"team_name":"e2e-team-demo"}' --json
omx team api write-shutdown-request --input '{"team_name":"e2e-team-demo","worker":"worker-1","requested_by":"leader-fixed"}' --json
omx team api read-shutdown-ack --input '{"team_name":"e2e-team-demo","worker":"worker-1"}' --json
omx team api read-monitor-snapshot --input '{"team_name":"e2e-team-demo"}' --json