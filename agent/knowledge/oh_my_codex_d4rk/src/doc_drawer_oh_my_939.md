turns_without_progress === 'number'
      ? ` turns_without_progress=${item.turns_without_progress}`
      : '';
    const lastTurnPart = item.last_turn_at ? ` last_turn_at=${item.last_turn_at}` : '';
    const statusUpdatedPart = item.status_updated_at ? ` status_updated_at=${item.status_updated_at}` : '';
    const pidPart = typeof item.pid === 'number' ? ` pid=${item.pid}` : '';
    const worktreeRepoRootPart = item.worktree_repo_root ? ` worktree_repo_root=${item.worktree_repo_root}` : '';
    const worktreePathPart = item.worktree_path ? ` worktree_path=${item.worktree_path}` : '';
    const worktreeBranchPart = item.worktree_branch ? ` worktree_branch=${item.worktree_branch}` : '';
    const worktreeDetachedPart = typeof item.worktree_detached === 'boolean'