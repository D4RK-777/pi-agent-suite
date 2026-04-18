approvalReviewerPart = item.approval_reviewer ? ` approval_reviewer=${item.approval_reviewer}` : '';
    const approvalReasonPart = item.approval_reason ? ` approval_reason=${item.approval_reason}` : '';
    const approvalDecidedAtPart = item.approval_decided_at ? ` approval_decided_at=${item.approval_decided_at}` : '';
    const approvalRecordPresentPart = typeof item.approval_record_present === 'boolean'
      ? ` approval_record_present=${item.approval_record_present}`
      : '';
    const statePart = item.state ? ` state=${item.state}` : '';
    const stateReasonPart = item.state_reason ? ` state_reason=${item.state_reason}` : '';
    const taskPart = item.task_id ? ` task=${item.task_id}` : '';
    const subjectPart = item.task_subject ? ` subject=${item.task_subject}` : '';