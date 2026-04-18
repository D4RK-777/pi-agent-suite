, /stale_leader/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('does not emit stale_leader when HUD state is fresh', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-team-'));
    try {
      const teamRoot = join(wd, '.omx', 'state', 'team', 'zeta');
      await mkdir(join(teamRoot, 'workers', 'worker-1'), { recursive: true });
      await writeFile(join(teamRoot, 'config.json'), JSON.stringify({
        name: 'zeta',
        tmux_session: 'omx-team-zeta',
      }));

      // Fresh HUD state (leader active 10 seconds ago)
      await writeFile(join(wd, '.omx', 'state', 'hud-state.json'), JSON.stringify({
        last_turn_at: new Date(Date.now() - 10_000).toISOString(),
        turn_count: 20,
      }));