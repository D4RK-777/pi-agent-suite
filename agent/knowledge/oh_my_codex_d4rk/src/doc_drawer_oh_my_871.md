candidate.name === target);
      return [target, worker?.worktree_repo_root ?? null];
    }),
  );
  const recommendedInspectWorktreeBranches = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.worktree_branch ?? null];
    }),
  );
  const recommendedInspectWorktreeDetached = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.worktree_detached ?? null];
    }),
  );
  const recommendedInspectWorktreeCreated = Object.fromEntries(
    recommendedInspectTargets.map((target) => {