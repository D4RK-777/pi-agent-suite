ENTS.md')), true);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('exposes help for agents-init and the deepinit alias', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-init-'));
    try {
      const helpRes = runOmx(wd, ['agents-init', '--help']);
      if (shouldSkipForSpawnPermissions(helpRes.error)) return;
      assert.equal(helpRes.status, 0, helpRes.stderr || helpRes.stdout);
      assert.match(helpRes.stdout, /Usage: omx agents-init/);