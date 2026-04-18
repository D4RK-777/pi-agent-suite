0, helpRes.stderr || helpRes.stdout);
      assert.match(helpRes.stdout, /Usage: omx agents-init/);

      const aliasRes = runOmx(wd, ['deepinit', '--help']);
      if (shouldSkipForSpawnPermissions(aliasRes.error)) return;
      assert.equal(aliasRes.status, 0, aliasRes.stderr || aliasRes.stdout);
      assert.match(aliasRes.stdout, /Usage: omx agents-init/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});