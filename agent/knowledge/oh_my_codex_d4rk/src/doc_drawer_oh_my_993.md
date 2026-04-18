me: runtime.teamName,
    });
    const availableAgentTypes = await resolveAvailableAgentTypes(cwd);
    const staffingPlan = buildFollowupStaffingPlan('team', runtime.config.task, availableAgentTypes, {
      workerCount: runtime.config.worker_count,
      fallbackRole: resolveImplicitTeamFallbackRole(runtime.config.agent_type, false),
    });
    await renderStartSummary(runtime, staffingPlan);
    return;
  }