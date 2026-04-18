(taskId) ?? []) : []];
    }),
  );
  const recommendedInspectTaskClaimPresent = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskClaimPresentById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskClaimOwners = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskClaimOwnerById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskClaimTokens = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];