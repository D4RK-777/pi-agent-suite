mpletedAt) {
      console.log(`inspect_task_completed_at_${target}: ${taskCompletedAt}`);
    }
  }
  for (const [target, taskDependsOn] of Object.entries(paneStatus.recommended_inspect_task_depends_on)) {
    if (taskDependsOn.length > 0) {
      console.log(`inspect_task_depends_on_${target}: ${taskDependsOn.join(' ')}`);
    }
  }
  for (const [target, taskClaimPresent] of Object.entries(paneStatus.recommended_inspect_task_claim_present)) {
    if (typeof taskClaimPresent === 'boolean') {
      console.log(`inspect_task_claim_present_${target}: ${taskClaimPresent}`);
    }
  }
  for (const [target, taskClaimOwner] of Object.entries(paneStatus.recommended_inspect_task_claim_owners)) {
    if (taskClaimOwner) {
      console.log(`inspect_task_claim_owner_${target}: ${taskClaimOwner}`);