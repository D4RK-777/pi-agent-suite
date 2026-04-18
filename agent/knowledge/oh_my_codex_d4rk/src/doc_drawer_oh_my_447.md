{
        // ignore malformed manifest
      }
    } else if (existsSync(configPath)) {
      try {
        const raw = await readFile(configPath, 'utf-8');
        const parsed = JSON.parse(raw) as { tmux_session?: string };
        if (typeof parsed.tmux_session === 'string' && parsed.tmux_session.trim() !== '') {
          tmuxSession = parsed.tmux_session;
        }
      } catch {
        // ignore malformed config
      }
    }

    knownTeamSessions.add(tmuxSession);

    // resume_blocker: only meaningful if tmux is available to query
    if (!tmuxUnavailable && !tmuxSessions.has(tmuxSession)) {
      issues.push({
        code: 'resume_blocker',
        message: `${teamName} references missing tmux session ${tmuxSession}`,
        severity: 'fail',
      });
    }