, arch: process.arch }));
        spawnSync('chmod', ['+x', packagedBinary], { encoding: 'utf-8' });

        try {
          const res = runOmx(wd, ['doctor'], {
            HOME: home,
            CODEX_HOME: join(home, '.codex'),
            PATH: fakeBin,
          });
          if (shouldSkipForSpawnPermissions(res.error)) return;
          assert.equal(res.status, 0, res.stderr || res.stdout);
          assert.match(
            res.stdout,
            /Explore Harness: ready \(packaged native binary:/,
          );
        } finally {
          if (originalBinary) {
            await writeFile(packagedBinary, originalBinary);
            spawnSync('chmod', ['+x', packagedBinary], { encoding: 'utf-8' });
          } else {
            await rm(packagedBinary, { force: true });