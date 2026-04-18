)) {
    if (taskOwner) {
      console.log(`inspect_task_owner_${target}: ${taskOwner}`);
    }
  }
  for (const [target, approvalStatus] of Object.entries(paneStatus.recommended_inspect_approval_statuses)) {
    if (approvalStatus) {
      console.log(`inspect_approval_status_${target}: ${approvalStatus}`);
    }
  }
  for (const [target, approvalReviewer] of Object.entries(paneStatus.recommended_inspect_approval_reviewers)) {
    if (approvalReviewer) {
      console.log(`inspect_approval_reviewer_${target}: ${approvalReviewer}`);
    }
  }
  for (const [target, approvalReason] of Object.entries(paneStatus.recommended_inspect_approval_reasons)) {
    if (approvalReason) {
      console.log(`inspect_approval_reason_${target}: ${approvalReason}`);
    }
  }