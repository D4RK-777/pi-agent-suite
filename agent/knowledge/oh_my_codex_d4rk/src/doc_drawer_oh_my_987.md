utIdx = teamArgs.indexOf('--timeout-ms');
    const afterIdx = teamArgs.indexOf('--after-event-id');
    const timeoutMs = timeoutIdx >= 0 && teamArgs[timeoutIdx + 1]
      ? Math.max(1, Number.parseInt(teamArgs[timeoutIdx + 1]!, 10) || 0)
      : 30_000;
    const afterEventId = afterIdx >= 0 ? (teamArgs[afterIdx + 1] || '') : '';
    const config = await readTeamConfig(name, cwd);
    if (!config) {
      if (wantsJson) {
        console.log(JSON.stringify({ team_name: name, status: 'missing', cursor: afterEventId || '', event: null }));
      } else {
        console.log(`No team state found for ${name}`);
      }
      return;
    }