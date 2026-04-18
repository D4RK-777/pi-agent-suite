worktree_branch}` : '';
    const worktreeDetachedPart = typeof item.worktree_detached === 'boolean'
      ? ` worktree_detached=${item.worktree_detached}`
      : '';
    const worktreeCreatedPart = typeof item.worktree_created === 'boolean'
      ? ` worktree_created=${item.worktree_created}`
      : '';
    const teamStateRootPart = item.team_state_root ? ` team_state_root=${item.team_state_root}` : '';
    const workdirPart = item.working_dir ? ` workdir=${item.working_dir}` : '';
    const assignedTasksPart = item.assigned_tasks.length > 0 ? ` assigned_tasks=${item.assigned_tasks.join(',')}` : '';
    const taskStatusPart = item.task_status ? ` task_status=${item.task_status}` : '';
    const taskResultPart = item.task_result ? ` task_result=${item.task_result}` : '';