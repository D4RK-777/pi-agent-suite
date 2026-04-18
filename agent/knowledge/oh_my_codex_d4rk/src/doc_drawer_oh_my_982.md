code=${envelope.error.code}: ${envelope.error.message}`);
    process.exitCode = 1;
    return;
  }

  if (subcommand === 'status') {
    const name = teamArgs[1];
    const wantsJson = teamArgs.includes('--json');
    if (!name) throw new Error('Usage: omx team status <team-name> [--json]');
    await recordLeaderRuntimeActivity(cwd, 'team_status', name);
    const snapshot = await monitorTeam(name, cwd);
    if (!snapshot) {
      if (wantsJson) {
        console.log(JSON.stringify({
          ...buildJsonBase(),
          command: 'omx team status',
          team_name: name,
          status: 'missing',
        }));
        return;
      }
      console.log(`No team state found for ${name}`);
      return;
    }
    const tailLines = parseStatusTailLines(teamArgs.slice(2));