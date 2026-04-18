date_missing/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('handles interrupted, evaluator failure, and evaluator parse-error branches', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const worktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t080000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t080000z', worktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);