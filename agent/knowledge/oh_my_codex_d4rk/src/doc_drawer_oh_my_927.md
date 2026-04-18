escription] of Object.entries(paneStatus.recommended_inspect_descriptions)) {
    if (description) {
      console.log(`inspect_description_${target}: ${description}`);
    }
  }
  for (const [target, blockedBy] of Object.entries(paneStatus.recommended_inspect_blocked_by)) {
    if (blockedBy.length > 0) {
      console.log(`inspect_blocked_by_${target}: ${blockedBy.join(' ')}`);
    }
  }
  for (const [target, taskRole] of Object.entries(paneStatus.recommended_inspect_task_roles)) {
    if (taskRole) {
      console.log(`inspect_task_role_${target}: ${taskRole}`);
    }
  }
  for (const [target, taskOwner] of Object.entries(paneStatus.recommended_inspect_task_owners)) {
    if (taskOwner) {
      console.log(`inspect_task_owner_${target}: ${taskOwner}`);
    }
  }