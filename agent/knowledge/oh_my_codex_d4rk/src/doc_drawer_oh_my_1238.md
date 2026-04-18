"codex test"\n');
        spawnSync('chmod', ['+x', join(fakeBin, 'codex')], { encoding: 'utf-8' });

        const res = runOmx(wd, ['doctor'], {
          HOME: home,
          CODEX_HOME: join(home, '.codex'),
          PATH: fakeBin,
        });
        if (shouldSkipForSpawnPermissions(res.error)) return;
        assert.equal(res.status, 0, res.stderr || res.stdout);
        assert.match(
          res.stdout,
          /Explore Harness: (Rust harness sources are packaged, but no compatible packaged prebuilt or cargo was found \(install Rust or set OMX_EXPLORE_BIN for omx explore\)|not ready \(no packaged binary, OMX_EXPLORE_BIN, or cargo toolchain\))/,
        );
      });
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });