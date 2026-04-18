fig.agent_type, false),
    });
    await renderStartSummary(runtime, staffingPlan);
    return;
  }

  if (subcommand === 'shutdown') {
    const name = teamArgs[1];
    if (!name) throw new Error('Usage: omx team shutdown <team-name> [--force]');
    const force = teamArgs.includes('--force');
    await shutdownTeam(name, cwd, { force });
    await updateModeState('team', {
      active: false,
      current_phase: 'cancelled',
      completed_at: new Date().toISOString(),
    }).catch((error: unknown) => {
      console.warn('[omx] warning: failed to persist team mode shutdown state', {
        team: name,
        error: error instanceof Error ? error.message : String(error),
      });
    });
    console.log(`Team shutdown complete: ${name}`);
    return;
  }