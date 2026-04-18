, /stale_leader/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('does not emit orphan_tmux_session when tmux reports no server running', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-team-'));
    try {
      const fakeBin = join(wd, 'bin');
      await mkdir(fakeBin, { recursive: true });
      const tmuxPath = join(fakeBin, 'tmux');
      await writeFile(
        tmuxPath,
        '#!/bin/sh\nif [ "$1" = "list-sessions" ]; then echo "no server running on /tmp/tmux-1000/default" 1>&2; exit 1; fi\nexit 0\n',
      );
      spawnSync('chmod', ['+x', tmuxPath], { encoding: 'utf-8' });