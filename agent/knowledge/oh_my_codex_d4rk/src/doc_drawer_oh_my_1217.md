writeFile(join(workerDir, 'shutdown-request.json'), JSON.stringify({ requested_at: requestedAt }));

      const fakeBin = await createFakeTmuxBin(wd, '#!/bin/sh\n# list-sessions success with no sessions\nexit 0\n');
      const res = runOmx(wd, ['doctor', '--team'], { PATH: `${fakeBin}:${process.env.PATH || ''}` });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 1, res.stderr || res.stdout);
      assert.match(res.stdout, /slow_shutdown/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });