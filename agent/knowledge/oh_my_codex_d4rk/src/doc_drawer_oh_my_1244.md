{ recursive: true });
      await writeFile(
        join(codexDir, 'config.toml'),
        `
[env]
USE_OMX_EXPLORE_CMD = "off"
`.trimStart(),
      );

      const res = runOmx(wd, ['doctor'], {
        HOME: home,
        CODEX_HOME: join(home, '.codex'),
      });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.match(
        res.stdout,
        /Explore routing: disabled in config\.toml \[env\]; set USE_OMX_EXPLORE_CMD = "1" to restore default explore-first routing/,
      );
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });