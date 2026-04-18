, /stale_leader/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('does not emit stale_leader when leader recently checked team status', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-team-'));
    try {
      const stateDir = join(wd, '.omx', 'state');
      const teamRoot = join(stateDir, 'team', 'eta');
      await mkdir(join(teamRoot, 'workers', 'worker-1'), { recursive: true });
      await writeFile(join(teamRoot, 'config.json'), JSON.stringify({
        name: 'eta',
        tmux_session: 'omx-team-eta',
      }));