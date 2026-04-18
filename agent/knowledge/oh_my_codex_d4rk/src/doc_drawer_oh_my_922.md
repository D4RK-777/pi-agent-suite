Object.entries(paneStatus.recommended_inspect_assigned_tasks)) {
    if (assignedTasks.length > 0) {
      console.log(`inspect_assigned_tasks_${target}: ${assignedTasks.join(' ')}`);
    }
  }
  for (const [target, taskStatus] of Object.entries(paneStatus.recommended_inspect_task_statuses)) {
    if (taskStatus) {
      console.log(`inspect_task_status_${target}: ${taskStatus}`);
    }
  }
  for (const [target, taskResult] of Object.entries(paneStatus.recommended_inspect_task_results)) {
    if (taskResult) {
      console.log(`inspect_task_result_${target}: ${taskResult}`);
    }
  }
  for (const [target, taskError] of Object.entries(paneStatus.recommended_inspect_task_errors)) {
    if (taskError) {
      console.log(`inspect_task_error_${target}: ${taskError}`);
    }
  }