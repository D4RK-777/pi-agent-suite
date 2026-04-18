nspect_states)) {
    if (state) {
      console.log(`inspect_state_${target}: ${state}`);
    }
  }
  for (const [target, stateReason] of Object.entries(paneStatus.recommended_inspect_state_reasons)) {
    if (stateReason) {
      console.log(`inspect_state_reason_${target}: ${stateReason}`);
    }
  }
  for (const [target, taskId] of Object.entries(paneStatus.recommended_inspect_tasks)) {
    if (taskId) {
      console.log(`inspect_task_${target}: ${taskId}`);
    }
  }
  for (const [target, subject] of Object.entries(paneStatus.recommended_inspect_subjects)) {
    if (subject) {
      console.log(`inspect_subject_${target}: ${subject}`);
    }
  }
  for (const [target, taskPath] of Object.entries(paneStatus.recommended_inspect_task_paths)) {
    if (taskPath) {