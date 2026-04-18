recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskClaimTokenById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskClaimLeases = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskClaimLeaseById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskClaimLockPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId && snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'claims', `task-${taskId}.lock`) : null];
    }),
  );