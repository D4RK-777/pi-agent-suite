teTasksToWorkers(tasks, workers).map(({ allocation_reason: _allocationReason, ...task }) => task);
}

async function ensureTeamModeState(
  parsed: ParsedTeamArgs,
  tasks?: Array<{ role?: string }>,
): Promise<void> {
  const fallbackRole = resolveImplicitTeamFallbackRole(parsed.agentType, parsed.explicitAgentType);
  const roleDistribution = tasks && tasks.length > 0
    ? [...new Set(tasks.map(t => t.role ?? parsed.agentType))].join(',')
    : parsed.agentType;

  const availableAgentTypes = await resolveAvailableAgentTypes(process.cwd());
  const staffingPlan = buildFollowupStaffingPlan('team', parsed.task, availableAgentTypes, {
    workerCount: parsed.workerCount,
    fallbackRole,
  });