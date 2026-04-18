m', parsed.task, availableAgentTypes, {
    workerCount: parsed.workerCount,
    fallbackRole,
  });

  const existing = await readModeState('team');
  if (existing?.active) {
    await updateModeState('team', {
      task_description: parsed.task,
      current_phase: 'team-exec',
      team_name: parsed.teamName,
      agent_count: parsed.workerCount,
      agent_types: roleDistribution,
      available_agent_types: availableAgentTypes,
      staffing_summary: staffingPlan.staffingSummary,
      staffing_allocations: staffingPlan.allocations,
    });
    return;
  }