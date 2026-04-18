im();
  if (!task) {
    throw new Error('Usage: omx team [N:agent-type] "<task description>"');
  }

  const followupContext = resolveApprovedTeamFollowupContext(cwd, task);
  const effectiveTask = followupContext?.task ?? task;
  if (followupContext) {
    if (!explicitWorkerCount) {
      workerCount = followupContext.workerCount;
      explicitWorkerCount = followupContext.explicitWorkerCount;
    }
    if (!explicitAgentType && followupContext.agentType) {
      agentType = followupContext.agentType;
      explicitAgentType = followupContext.explicitAgentType === true;
    }
  }

  const teamName = sanitizeTeamName(slugifyTask(effectiveTask));
  return { workerCount, agentType, explicitAgentType, explicitWorkerCount, task: effectiveTask, teamName };
}