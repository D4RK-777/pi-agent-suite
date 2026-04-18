-cli-'));
    const home = join(wd, 'home');
    try {
      await mkdir(home, { recursive: true });

      const result = runOmx(wd, ['agents', 'add', 'my-helper', '--scope', 'project'], {
        HOME: home,
        CODEX_HOME: join(home, '.codex'),
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;

      assert.equal(result.status, 0, result.stderr || result.stdout);
      const agentPath = join(wd, '.codex', 'agents', 'my-helper.toml');
      assert.equal(existsSync(agentPath), true);