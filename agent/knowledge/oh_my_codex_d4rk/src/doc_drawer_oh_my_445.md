});
      }
    }
    if (authority?.stale) {
      issues.push({
        code: 'stale_leader',
        message: `authority stale (owner: ${authority.owner ?? 'unknown'}): ${authority.stale_reason ?? 'unknown reason'}`,
        severity: 'fail',
      });
    }
  }

  const teamDirs: string[] = [];
  if (existsSync(teamsRoot)) {
    const entries = await readdir(teamsRoot, { withFileTypes: true });
    for (const e of entries) {
      if (e.isDirectory()) teamDirs.push(e.name);
    }
  }

  const tmuxSessions = listTeamTmuxSessions();
  const tmuxUnavailable = tmuxSessions === null;
  const knownTeamSessions = new Set<string>();