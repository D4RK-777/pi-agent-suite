StaffingPlan('team', parsed.task, availableAgentTypes, {
    workerCount: executionPlan.workerCount,
    fallbackRole: resolveImplicitTeamFallbackRole(parsed.agentType, parsed.explicitAgentType),
  });
  const runtime = await startTeam(
    parsed.teamName,
    parsed.task,
    parsed.agentType,
    executionPlan.workerCount,
    tasks,
    cwd,
    { worktreeMode },
  );

  await ensureTeamModeState(effectiveParsed, tasks);
  await renderStartSummary(runtime, staffingPlan);
}