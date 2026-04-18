recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskCreatedAtById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskCompletedAt = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskCompletedAtById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskDependsOn = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskDependsOnById.get(taskId) ?? []) : []];
    }),
  );
  const recommendedInspectTaskClaimPresent = Object.fromEntries(