st [target, workerInboxPath] of Object.entries(paneStatus.recommended_inspect_worker_inbox_paths)) {
    if (workerInboxPath) {
      console.log(`inspect_worker_inbox_path_${target}: ${workerInboxPath}`);
    }
  }
  for (const [target, workerMailboxPath] of Object.entries(paneStatus.recommended_inspect_worker_mailbox_paths)) {
    if (workerMailboxPath) {
      console.log(`inspect_worker_mailbox_path_${target}: ${workerMailboxPath}`);
    }
  }
  for (const [target, workerShutdownRequestPath] of Object.entries(paneStatus.recommended_inspect_worker_shutdown_request_paths)) {
    if (workerShutdownRequestPath) {
      console.log(`inspect_worker_shutdown_request_path_${target}: ${workerShutdownRequestPath}`);
    }
  }