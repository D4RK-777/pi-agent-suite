gPlan.staffingSummary,
      staffing_allocations: staffingPlan.allocations,
    });
    return;
  }

  await startMode('team', parsed.task, 50);
  await updateModeState('team', {
    current_phase: 'team-exec',
    team_name: parsed.teamName,
    agent_count: parsed.workerCount,
    agent_types: roleDistribution,
    available_agent_types: availableAgentTypes,
    staffing_summary: staffingPlan.staffingSummary,
    staffing_allocations: staffingPlan.allocations,
  });

}