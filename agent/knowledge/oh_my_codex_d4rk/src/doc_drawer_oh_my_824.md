const approvedHint = readApprovedExecutionLaunchHint(cwd, 'team');
  if (!approvedHint) return null;

  const persistedTask = typeof existingTeamState?.task_description === 'string'
    ? existingTeamState.task_description
    : typeof existingTeamState?.task === 'string'
      ? existingTeamState.task
      : null;
  const persistedWorkerCount = typeof existingTeamState?.agent_count === 'number'
    ? existingTeamState.agent_count
    : typeof existingTeamState?.workerCount === 'number'
      ? existingTeamState.workerCount
      : null;
  if (persistedTask && persistedWorkerCount && persistedTask.trim() === approvedHint.task.trim()) {
    return {
      task: persistedTask,
      workerCount: persistedWorkerCount,
      explicitWorkerCount: true,
      agentType: approvedHint.agentType,