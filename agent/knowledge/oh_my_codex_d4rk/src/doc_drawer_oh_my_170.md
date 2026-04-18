.throws(() => assertResetSafeWorktree(worktreePath), /autoresearch_reset_requires_clean_worktree/i);

      const manifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      assert.equal(manifest.results_file, join(worktreePath, 'results.tsv'));
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('rejects concurrent fresh runs via the repo-root active-run lock', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const worktreePathA = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t030000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t030000z', worktreePathA, 'HEAD'], {
        cwd: repo,