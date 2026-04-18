tatus}` : '';
    const taskResultPart = item.task_result ? ` task_result=${item.task_result}` : '';
    const taskErrorPart = item.task_error ? ` task_error=${item.task_error}` : '';
    const taskVersionPart = typeof item.task_version === 'number' ? ` task_version=${item.task_version}` : '';
    const taskCreatedAtPart = item.task_created_at ? ` task_created_at=${item.task_created_at}` : '';
    const taskCompletedAtPart = item.task_completed_at ? ` task_completed_at=${item.task_completed_at}` : '';
    const taskDependsOnPart = item.task_depends_on.length > 0 ? ` task_depends_on=${item.task_depends_on.join(',')}` : '';
    const taskClaimPresentPart = typeof item.task_claim_present === 'boolean'
      ? ` task_claim_present=${item.task_claim_present}`
      : '';