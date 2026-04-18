s[target];
      return [target, taskId ? (taskResultById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskErrors = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskErrorById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskVersions = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskVersionById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskCreatedAt = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];