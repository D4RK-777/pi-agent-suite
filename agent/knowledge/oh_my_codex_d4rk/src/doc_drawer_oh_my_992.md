cursor=${result.cursor}`,
    ].filter(Boolean).join(' ');
    console.log(context);
    return;
  }

  if (subcommand === 'resume') {
    const name = teamArgs[1];
    if (!name) throw new Error('Usage: omx team resume <team-name>');
    const runtime = await resumeTeam(name, cwd);
    if (!runtime) {
      console.log(`No resumable team found for ${name}`);
      return;
    }
    await ensureTeamModeState({
      task: runtime.config.task,
      workerCount: runtime.config.worker_count,
      agentType: runtime.config.agent_type,
      explicitAgentType: false,
      explicitWorkerCount: false,
      teamName: runtime.teamName,
    });
    const availableAgentTypes = await resolveAvailableAgentTypes(cwd);