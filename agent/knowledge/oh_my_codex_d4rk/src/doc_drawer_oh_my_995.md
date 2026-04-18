String(error),
      });
    });
    console.log(`Team shutdown complete: ${name}`);
    return;
  }

  const parsed = parseTeamArgs(teamArgs, cwd);
  const executionPlan = buildTeamExecutionPlan(
    parsed.task,
    parsed.workerCount,
    parsed.agentType,
    parsed.explicitAgentType,
    parsed.explicitWorkerCount,
  );
  const tasks = executionPlan.tasks;
  const effectiveParsed = executionPlan.workerCount === parsed.workerCount
    ? parsed
    : { ...parsed, workerCount: executionPlan.workerCount };
  const availableAgentTypes = await resolveAvailableAgentTypes(cwd);
  const staffingPlan = buildFollowupStaffingPlan('team', parsed.task, availableAgentTypes, {
    workerCount: executionPlan.workerCount,