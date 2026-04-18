n', 'utf-8');
      await writeFile(join(repo, '.omx', 'state', 'hud-state.json'), '{}\n', 'utf-8');

      assert.doesNotThrow(() => assertResetSafeWorktree(repo));
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('prepares runtime artifacts and persists autoresearch mode state', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      await mkdir(join(repo, 'node_modules', 'fixture-dep'), { recursive: true });
      await writeFile(join(repo, 'node_modules', 'fixture-dep', 'index.js'), 'export default 1;\n', 'utf-8');
      const worktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t000000z');