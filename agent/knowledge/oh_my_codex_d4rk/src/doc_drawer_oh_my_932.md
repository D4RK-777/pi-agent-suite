of Object.entries(paneStatus.recommended_inspect_worker_status_paths)) {
    if (workerStatusPath) {
      console.log(`inspect_worker_status_path_${target}: ${workerStatusPath}`);
    }
  }
  for (const [target, workerHeartbeatPath] of Object.entries(paneStatus.recommended_inspect_worker_heartbeat_paths)) {
    if (workerHeartbeatPath) {
      console.log(`inspect_worker_heartbeat_path_${target}: ${workerHeartbeatPath}`);
    }
  }
  for (const [target, workerIdentityPath] of Object.entries(paneStatus.recommended_inspect_worker_identity_paths)) {
    if (workerIdentityPath) {
      console.log(`inspect_worker_identity_path_${target}: ${workerIdentityPath}`);
    }
  }
  for (const [target, workerInboxPath] of Object.entries(paneStatus.recommended_inspect_worker_inbox_paths)) {