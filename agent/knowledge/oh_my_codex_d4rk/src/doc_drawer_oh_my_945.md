em.task_id}` : '';
    const subjectPart = item.task_subject ? ` subject=${item.task_subject}` : '';
    const taskPathPart = item.task_path ? ` task_path=${item.task_path}` : '';
    const approvalPathPart = item.approval_path ? ` approval_path=${item.approval_path}` : '';
    const workerStateDirPart = item.worker_state_dir ? ` worker_state_dir=${item.worker_state_dir}` : '';
    const workerStatusPathPart = item.worker_status_path ? ` worker_status_path=${item.worker_status_path}` : '';
    const workerHeartbeatPathPart = item.worker_heartbeat_path ? ` worker_heartbeat_path=${item.worker_heartbeat_path}` : '';
    const workerIdentityPathPart = item.worker_identity_path ? ` worker_identity_path=${item.worker_identity_path}` : '';