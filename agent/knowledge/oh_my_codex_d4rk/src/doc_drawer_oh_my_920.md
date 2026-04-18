of Object.entries(paneStatus.recommended_inspect_worktree_repo_roots)) {
    if (worktreeRepoRoot) {
      console.log(`inspect_worktree_repo_root_${target}: ${worktreeRepoRoot}`);
    }
  }
  for (const [target, worktreeBranch] of Object.entries(paneStatus.recommended_inspect_worktree_branches)) {
    if (worktreeBranch) {
      console.log(`inspect_worktree_branch_${target}: ${worktreeBranch}`);
    }
  }
  for (const [target, worktreeDetached] of Object.entries(paneStatus.recommended_inspect_worktree_detached)) {
    if (typeof worktreeDetached === 'boolean') {
      console.log(`inspect_worktree_detached_${target}: ${worktreeDetached}`);
    }
  }
  for (const [target, worktreeCreated] of Object.entries(paneStatus.recommended_inspect_worktree_created)) {