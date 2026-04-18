((snapshot?.tasks.items ?? []).map((task) => [task.id, task.claim?.leased_until ?? null] as const));
  const taskRequiresCodeChangeById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.requires_code_change ?? null] as const));
  const recommendedInspectTaskStatuses = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskStatusById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskResults = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskResultById.get(taskId) ?? null) : null];
    }),
  );