owMs - reqMs > shutdownThresholdMs) {
            issues.push({
              code: 'slow_shutdown',
              message: `${teamName}/${worker.name} has stale shutdown request without ack`,
              severity: 'fail',
            });
          }
        } catch {
          // ignore malformed files
        }
      }
    }
  }

  // stale_leader: team has active workers but leader has no recent activity
  const hudStatePath = join(stateDir, 'hud-state.json');
  const leaderActivityPath = join(stateDir, 'leader-runtime-activity.json');
  if ((existsSync(hudStatePath) || existsSync(leaderActivityPath)) && teamDirs.length > 0) {
    try {
      const leaderIsStale = await isLeaderRuntimeStale(stateDir, leaderStaleThresholdMs, nowMs);