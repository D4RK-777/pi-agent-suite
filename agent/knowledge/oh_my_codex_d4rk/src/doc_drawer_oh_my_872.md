ommendedInspectWorktreeCreated = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.worktree_created ?? null];
    }),
  );
  const recommendedInspectTeamStateRoots = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.team_state_root ?? null];
    }),
  );
  const recommendedInspectWorkdirs = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.working_dir ?? worker?.worktree_path ?? null];
    }),
  );