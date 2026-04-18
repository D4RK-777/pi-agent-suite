5_000).toISOString(),
        last_source: 'team_status',
        last_team_name: 'eta',
      }));

      const fakeBin = join(wd, 'bin');
      await mkdir(fakeBin, { recursive: true });
      const tmuxPath = join(fakeBin, 'tmux');
      await writeFile(tmuxPath, '#!/bin/sh\nif [ "$1" = "list-sessions" ]; then echo "omx-team-eta"; exit 0; fi\nexit 0\n');
      spawnSync('chmod', ['+x', tmuxPath], { encoding: 'utf-8' });

      const res = runOmx(wd, ['doctor', '--team'], { PATH: `${fakeBin}:${process.env.PATH || ''}` });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.doesNotMatch(res.stdout, /stale_leader/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });