nd for ${name}`);
      return;
    }
    const tailLines = parseStatusTailLines(teamArgs.slice(2));
    const config = await readTeamConfig(name, cwd);
    const paneStatus = await readTeamPaneStatus(config, cwd, snapshot, tailLines);
    if (wantsJson) {
      console.log(JSON.stringify({
        ...buildJsonBase(),
        command: 'omx team status',
        team_name: snapshot.teamName,
        status: 'ok',
        tail_lines: tailLines,
        phase: snapshot.phase,
        workspace_mode: config?.workspace_mode ?? null,
        dead_workers: snapshot.deadWorkers,
        non_reporting_workers: snapshot.nonReportingWorkers,
        workers: {
          total: snapshot.workers.length,
          dead: snapshot.deadWorkers.length,