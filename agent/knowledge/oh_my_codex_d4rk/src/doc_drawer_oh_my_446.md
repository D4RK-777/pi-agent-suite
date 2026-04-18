s();
  const tmuxUnavailable = tmuxSessions === null;
  const knownTeamSessions = new Set<string>();

  for (const teamName of teamDirs) {
    const teamDir = join(teamsRoot, teamName);
    const manifestPath = join(teamDir, 'manifest.v2.json');
    const configPath = join(teamDir, 'config.json');

    let tmuxSession = `omx-team-${teamName}`;
    if (existsSync(manifestPath)) {
      try {
        const raw = await readFile(manifestPath, 'utf-8');
        const parsed = JSON.parse(raw) as { tmux_session?: string };
        if (typeof parsed.tmux_session === 'string' && parsed.tmux_session.trim() !== '') {
          tmuxSession = parsed.tmux_session;
        }
      } catch {
        // ignore malformed manifest
      }
    } else if (existsSync(configPath)) {
      try {