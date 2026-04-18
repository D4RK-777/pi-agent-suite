y {
      const leaderIsStale = await isLeaderRuntimeStale(stateDir, leaderStaleThresholdMs, nowMs);

      if (leaderIsStale && !tmuxUnavailable) {
        // Check if any team tmux session has live worker panes
        for (const teamName of teamDirs) {
          const session = knownTeamSessions.has(`omx-team-${teamName}`)
            ? `omx-team-${teamName}`
            : [...knownTeamSessions].find(s => s.includes(teamName));
          if (!session || !tmuxSessions.has(session)) continue;
          issues.push({
            code: 'stale_leader',
            message: `${teamName} has active tmux session but leader has no recent activity`,
            severity: 'fail',
          });
        }
      }
    } catch {
      // ignore malformed HUD state
    }
  }