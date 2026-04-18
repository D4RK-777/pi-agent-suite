ityPathPart = item.worker_identity_path ? ` worker_identity_path=${item.worker_identity_path}` : '';
    const workerInboxPathPart = item.worker_inbox_path ? ` worker_inbox_path=${item.worker_inbox_path}` : '';
    const workerMailboxPathPart = item.worker_mailbox_path ? ` worker_mailbox_path=${item.worker_mailbox_path}` : '';
    const workerShutdownRequestPathPart = item.worker_shutdown_request_path ? ` worker_shutdown_request_path=${item.worker_shutdown_request_path}` : '';
    const workerShutdownAckPathPart = item.worker_shutdown_ack_path ? ` worker_shutdown_ack_path=${item.worker_shutdown_ack_path}` : '';
    const teamDirPathPart = item.team_dir_path ? ` team_dir_path=${item.team_dir_path}` : '';