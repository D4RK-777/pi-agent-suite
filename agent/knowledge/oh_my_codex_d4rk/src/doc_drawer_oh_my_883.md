recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskRoleById.get(taskId) ?? null) : null];
    }),
  );
  const taskOwnerById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.owner ?? null] as const));
  const recommendedInspectTaskOwners = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskOwnerById.get(taskId) ?? null) : null];
    }),
  );
  const approvalRecordByTaskId = new Map<string, Awaited<ReturnType<typeof readTaskApproval>>>();