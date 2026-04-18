HOME: join(home, '.codex'),
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;

      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stdout, /scope\s+name\s+model\s+description/i);
      assert.match(result.stdout, /project\s+planner\s+gpt-5\.4\s+Project planner/);
      assert.match(result.stdout, /user\s+reviewer\s+-\s+User reviewer/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('adds a scaffolded agent TOML file with required fields and commented optional fields', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-cli-'));
    const home = join(wd, 'home');
    try {
      await mkdir(home, { recursive: true });