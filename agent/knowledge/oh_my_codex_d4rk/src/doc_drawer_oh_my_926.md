Path) {
      console.log(`inspect_task_claim_lock_path_${target}: ${taskClaimLockPath}`);
    }
  }
  for (const [target, approvalRequired] of Object.entries(paneStatus.recommended_inspect_approval_required)) {
    if (typeof approvalRequired === 'boolean') {
      console.log(`inspect_approval_required_${target}: ${approvalRequired}`);
    }
  }
  for (const [target, requiresCodeChange] of Object.entries(paneStatus.recommended_inspect_requires_code_change)) {
    if (typeof requiresCodeChange === 'boolean') {
      console.log(`inspect_requires_code_change_${target}: ${requiresCodeChange}`);
    }
  }
  for (const [target, description] of Object.entries(paneStatus.recommended_inspect_descriptions)) {
    if (description) {