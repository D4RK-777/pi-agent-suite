)) {
    if (taskError) {
      console.log(`inspect_task_error_${target}: ${taskError}`);
    }
  }
  for (const [target, taskVersion] of Object.entries(paneStatus.recommended_inspect_task_versions)) {
    if (typeof taskVersion === 'number') {
      console.log(`inspect_task_version_${target}: ${taskVersion}`);
    }
  }
  for (const [target, taskCreatedAt] of Object.entries(paneStatus.recommended_inspect_task_created_at)) {
    if (taskCreatedAt) {
      console.log(`inspect_task_created_at_${target}: ${taskCreatedAt}`);
    }
  }
  for (const [target, taskCompletedAt] of Object.entries(paneStatus.recommended_inspect_task_completed_at)) {
    if (taskCompletedAt) {
      console.log(`inspect_task_completed_at_${target}: ${taskCompletedAt}`);
    }
  }