onst [target, worktreeCreated] of Object.entries(paneStatus.recommended_inspect_worktree_created)) {
    if (typeof worktreeCreated === 'boolean') {
      console.log(`inspect_worktree_created_${target}: ${worktreeCreated}`);
    }
  }
  for (const [target, teamStateRoot] of Object.entries(paneStatus.recommended_inspect_team_state_roots)) {
    if (teamStateRoot) {
      console.log(`inspect_team_state_root_${target}: ${teamStateRoot}`);
    }
  }
  for (const [target, workdir] of Object.entries(paneStatus.recommended_inspect_workdirs)) {
    if (workdir) {
      console.log(`inspect_workdir_${target}: ${workdir}`);
    }
  }
  for (const [target, assignedTasks] of Object.entries(paneStatus.recommended_inspect_assigned_tasks)) {
    if (assignedTasks.length > 0) {