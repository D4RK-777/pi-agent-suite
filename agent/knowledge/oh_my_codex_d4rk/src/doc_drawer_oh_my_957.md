.min(requestedWorkerCount, Math.max(2, plan.subtasks.length));
  }

  return requestedWorkerCount;
}

export function buildTeamExecutionPlan(
  task: string,
  workerCount: number,
  agentType: string,
  explicitAgentType: boolean,
  explicitWorkerCount = false,
): TeamExecutionPlan {
  const plan = splitTaskString(task);
  const effectiveWorkerCount = resolveTeamFanoutLimit(
    task,
    workerCount,
    explicitAgentType,
    explicitWorkerCount,
    plan,
  );
  const fallbackRole = resolveImplicitTeamFallbackRole(agentType, explicitAgentType);

  let subtasks = plan.subtasks;
  const usedAspectSubtasks = subtasks.length <= 1 && effectiveWorkerCount > 1;
  if (subtasks.length <= 1 && effectiveWorkerCount > 1) {
    subtasks = createAspectSubtasks(task, effectiveWorkerCount);
  }