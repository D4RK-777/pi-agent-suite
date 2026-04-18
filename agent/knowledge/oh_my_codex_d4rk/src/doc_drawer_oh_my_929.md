provalReason) {
      console.log(`inspect_approval_reason_${target}: ${approvalReason}`);
    }
  }
  for (const [target, approvalDecidedAt] of Object.entries(paneStatus.recommended_inspect_approval_decided_at)) {
    if (approvalDecidedAt) {
      console.log(`inspect_approval_decided_at_${target}: ${approvalDecidedAt}`);
    }
  }
  for (const [target, approvalRecordPresent] of Object.entries(paneStatus.recommended_inspect_approval_record_present)) {
    if (typeof approvalRecordPresent === 'boolean') {
      console.log(`inspect_approval_record_present_${target}: ${approvalRecordPresent}`);
    }
  }
  for (const [target, state] of Object.entries(paneStatus.recommended_inspect_states)) {
    if (state) {
      console.log(`inspect_state_${target}: ${state}`);
    }
  }