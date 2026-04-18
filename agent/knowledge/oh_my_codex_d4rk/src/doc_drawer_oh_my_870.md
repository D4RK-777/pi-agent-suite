const recommendedInspectPids = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.pid ?? null];
    }),
  );
  const recommendedInspectWorktreePaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.worktree_path ?? null];
    }),
  );
  const recommendedInspectWorktreeRepoRoots = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.worktree_repo_root ?? null];
    }),
  );