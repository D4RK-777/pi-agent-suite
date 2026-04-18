pid: 123,
        last_turn_at: lastTurnAt,
        turn_count: 10,
        alive: true,
      }));

      const fakeBin = await createFakeTmuxBin(wd, '#!/bin/sh\n# list-sessions success with no sessions\nexit 0\n');
      const res = runOmx(wd, ['doctor', '--team'], { PATH: `${fakeBin}:${process.env.PATH || ''}` });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 1, res.stderr || res.stdout);
      assert.match(res.stdout, /delayed_status_lag/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });