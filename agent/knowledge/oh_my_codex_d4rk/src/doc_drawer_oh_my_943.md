l_required}` : '';
    const requiresCodeChangePart = typeof item.requires_code_change === 'boolean'
      ? ` requires_code_change=${item.requires_code_change}`
      : '';
    const taskDescriptionPart = item.task_description ? ` description=${item.task_description}` : '';
    const blockedByPart = item.blocked_by.length > 0 ? ` blocked_by=${item.blocked_by.join(',')}` : '';
    const taskRolePart = item.task_role ? ` task_role=${item.task_role}` : '';
    const taskOwnerPart = item.task_owner ? ` task_owner=${item.task_owner}` : '';
    const approvalStatusPart = item.approval_status ? ` approval_status=${item.approval_status}` : '';
    const approvalReviewerPart = item.approval_reviewer ? ` approval_reviewer=${item.approval_reviewer}` : '';