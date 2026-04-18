xternal project/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('prints stale_leader when HUD state is old and team tmux session is active', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-team-'));
    try {
      const teamRoot = join(wd, '.omx', 'state', 'team', 'epsilon');
      await mkdir(join(teamRoot, 'workers', 'worker-1'), { recursive: true });
      await writeFile(join(teamRoot, 'config.json'), JSON.stringify({
        name: 'epsilon',
        tmux_session: 'omx-team-epsilon',
      }));