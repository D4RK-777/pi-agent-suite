&& effectiveWorkerCount > 1) {
    subtasks = createAspectSubtasks(task, effectiveWorkerCount);
  }

  const tasksWithRoles = subtasks.map((st) => {
    if (explicitAgentType) {
      return { ...st, role: agentType };
    }
    const result = routeTaskToRole(st.subject, st.description, 'team-exec', fallbackRole);
    return { ...st, role: result.role };
  });

  const normalizedRoles = new Set(tasksWithRoles.map((task) => (task.role ?? '').trim()));
  const tasks = usedAspectSubtasks && tasksWithRoles.length > 1 && normalizedRoles.size <= 1
    ? tasksWithRoles.map((task, index) => ({
      ...task,
      owner: `worker-${(index % effectiveWorkerCount) + 1}`,
    }))
    : distributeTasksToWorkers(
      tasksWithRoles,
      effectiveWorkerCount,