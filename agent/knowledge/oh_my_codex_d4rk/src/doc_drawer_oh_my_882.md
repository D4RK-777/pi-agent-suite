get];
      return [target, taskId ? (taskDescriptionById.get(taskId) ?? null) : null];
    }),
  );
  const taskBlockedById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.blocked_by ?? []] as const));
  const recommendedInspectBlockedBy = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskBlockedById.get(taskId) ?? []) : []];
    }),
  );
  const taskRoleById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.role ?? null] as const));
  const recommendedInspectTaskRoles = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];