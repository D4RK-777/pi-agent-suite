t];
      return [target, taskId ? approvalRecordByTaskId.get(taskId) !== null : null];
    }),
  );
  const recommendedInspectPanes = Object.fromEntries(
    recommendedInspectTargets.map((target) => [target, workerPanes[target] ?? null]),
  );
  const taskSubjectById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.subject] as const));
  const recommendedInspectSubjects = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (taskSubjectById.get(taskId) ?? null) : null];
    }),
  );
  const recommendedInspectTaskPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];