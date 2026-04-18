arget, taskPath] of Object.entries(paneStatus.recommended_inspect_task_paths)) {
    if (taskPath) {
      console.log(`inspect_task_path_${target}: ${taskPath}`);
    }
  }
  for (const [target, approvalPath] of Object.entries(paneStatus.recommended_inspect_approval_paths)) {
    if (approvalPath) {
      console.log(`inspect_approval_path_${target}: ${approvalPath}`);
    }
  }
  for (const [target, workerStateDir] of Object.entries(paneStatus.recommended_inspect_worker_state_dirs)) {
    if (workerStateDir) {
      console.log(`inspect_worker_state_dir_${target}: ${workerStateDir}`);
    }
  }
  for (const [target, workerStatusPath] of Object.entries(paneStatus.recommended_inspect_worker_status_paths)) {
    if (workerStatusPath) {