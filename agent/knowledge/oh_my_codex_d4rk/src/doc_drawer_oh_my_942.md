ask_claim_present === 'boolean'
      ? ` task_claim_present=${item.task_claim_present}`
      : '';
    const taskClaimOwnerPart = item.task_claim_owner ? ` task_claim_owner=${item.task_claim_owner}` : '';
    const taskClaimTokenPart = item.task_claim_token ? ` task_claim_token=${item.task_claim_token}` : '';
    const taskClaimLeasePart = item.task_claim_leased_until ? ` task_claim_leased_until=${item.task_claim_leased_until}` : '';
    const taskClaimLockPathPart = item.task_claim_lock_path ? ` task_claim_lock_path=${item.task_claim_lock_path}` : '';
    const approvalRequiredPart = typeof item.approval_required === 'boolean' ? ` approval_required=${item.approval_required}` : '';
    const requiresCodeChangePart = typeof item.requires_code_change === 'boolean'