= target);
      return [target, worker?.working_dir ?? worker?.worktree_path ?? null];
    }),
  );
  const recommendedInspectAssignedTasks = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.assigned_tasks ?? []];
    }),
  );
  const recommendedInspectTasks = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.status.current_task_id ?? null];
    }),
  );
  const taskStatusById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.status] as const));