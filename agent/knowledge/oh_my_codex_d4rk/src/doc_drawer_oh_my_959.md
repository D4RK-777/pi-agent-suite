nt) + 1}`,
    }))
    : distributeTasksToWorkers(
      tasksWithRoles,
      effectiveWorkerCount,
      explicitAgentType ? agentType : undefined,
    );

  return {
    workerCount: effectiveWorkerCount,
    tasks,
  };
}

export function decomposeTaskString(
  task: string,
  workerCount: number,
  agentType: string,
  explicitAgentType: boolean,
  explicitWorkerCount = false,
): Array<{ subject: string; description: string; owner: string; role?: string }> {
  return buildTeamExecutionPlan(task, workerCount, agentType, explicitAgentType, explicitWorkerCount).tasks;
}