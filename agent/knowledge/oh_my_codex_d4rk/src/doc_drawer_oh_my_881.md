, '.omx', 'state', 'team', snapshot.teamName, 'claims', `task-${taskId}.lock`) : null];
    }),
  );
  const recommendedInspectRequiresCodeChange = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskRequiresCodeChangeById.get(taskId) ?? null) : null];
    }),
  );
  const taskDescriptionById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.description] as const));
  const recommendedInspectDescriptions = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskDescriptionById.get(taskId) ?? null) : null];
    }),
  );