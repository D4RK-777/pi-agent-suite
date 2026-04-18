worker-1"}' --json
omx team api read-monitor-snapshot --input '{"team_name":"e2e-team-demo"}' --json
omx team api write-monitor-snapshot --input '{"team_name":"e2e-team-demo","snapshot":{"taskStatusById":{"1":"completed"},"workerAliveByName":{"worker-1":true},"workerStateByName":{"worker-1":"idle"},"workerTurnCountByName":{"worker-1":12},"workerTaskIdByName":{"worker-1":"1"},"mailboxNotifiedByMessageId":{},"completedEventTaskIds":{"1":true}}}' --json
omx team api read-task-approval --input '{"team_name":"e2e-team-demo","task_id":"<TASK_ID>"}' --json
omx team api write-task-approval --input '{"team_name":"e2e-team-demo","task_id":"<TASK_ID>","status":"approved","reviewer":"leader-fixed","decision_reason":"demo approval","required":true}' --json