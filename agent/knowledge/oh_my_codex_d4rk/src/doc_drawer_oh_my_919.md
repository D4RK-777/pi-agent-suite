t] of Object.entries(paneStatus.recommended_inspect_status_updated_at)) {
    if (statusUpdatedAt) {
      console.log(`inspect_status_updated_at_${target}: ${statusUpdatedAt}`);
    }
  }
  for (const [target, pid] of Object.entries(paneStatus.recommended_inspect_pids)) {
    if (typeof pid === 'number') {
      console.log(`inspect_pid_${target}: ${pid}`);
    }
  }
  for (const [target, worktreePath] of Object.entries(paneStatus.recommended_inspect_worktree_paths)) {
    if (worktreePath) {
      console.log(`inspect_worktree_path_${target}: ${worktreePath}`);
    }
  }
  for (const [target, worktreeRepoRoot] of Object.entries(paneStatus.recommended_inspect_worktree_repo_roots)) {
    if (worktreeRepoRoot) {