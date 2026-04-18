if (taskClaimOwner) {
      console.log(`inspect_task_claim_owner_${target}: ${taskClaimOwner}`);
    }
  }
  for (const [target, taskClaimToken] of Object.entries(paneStatus.recommended_inspect_task_claim_tokens)) {
    if (taskClaimToken) {
      console.log(`inspect_task_claim_token_${target}: ${taskClaimToken}`);
    }
  }
  for (const [target, taskClaimLease] of Object.entries(paneStatus.recommended_inspect_task_claim_leases)) {
    if (taskClaimLease) {
      console.log(`inspect_task_claim_leased_until_${target}: ${taskClaimLease}`);
    }
  }
  for (const [target, taskClaimLockPath] of Object.entries(paneStatus.recommended_inspect_task_claim_lock_paths)) {
    if (taskClaimLockPath) {
      console.log(`inspect_task_claim_lock_path_${target}: ${taskClaimLockPath}`);
    }
  }