/resume_blocker/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('prints slow_shutdown when shutdown request is stale and ack missing', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-team-'));
    try {
      const workerDir = join(wd, '.omx', 'state', 'team', 'beta', 'workers', 'worker-1');
      await mkdir(workerDir, { recursive: true });
      await writeFile(join(wd, '.omx', 'state', 'team', 'beta', 'config.json'), JSON.stringify({
        name: 'beta',
        tmux_session: 'omx-team-beta',
      }));

      const requestedAt = new Date(Date.now() - 60_000).toISOString();
      await writeFile(join(workerDir, 'shutdown-request.json'), JSON.stringify({ requested_at: requestedAt }));