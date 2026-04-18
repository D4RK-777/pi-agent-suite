recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId && snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'tasks', `task-${taskId}.json`) : null];
    }),
  );
  const recommendedInspectApprovalPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId && snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'approvals', `task-${taskId}.json`) : null];
    }),
  );
  const recommendedInspectWorkerStateDirs = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,