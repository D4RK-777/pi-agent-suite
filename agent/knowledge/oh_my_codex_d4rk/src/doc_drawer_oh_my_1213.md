g.json'), JSON.stringify({
        name: 'alpha',
        tmux_session: 'omx-team-alpha',
      }));

      const fakeBin = join(wd, 'bin');
      await mkdir(fakeBin, { recursive: true });
      const tmuxPath = join(fakeBin, 'tmux');
      await writeFile(tmuxPath, '#!/bin/sh\n# list-sessions success with no sessions\nexit 0\n');
      spawnSync('chmod', ['+x', tmuxPath], { encoding: 'utf-8' });

      const res = runOmx(wd, ['doctor', '--team'], { PATH: `${fakeBin}:${process.env.PATH || ''}` });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 1, res.stderr || res.stdout);
      assert.match(res.stdout, /resume_blocker/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });