ndidate abort');
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('rejects candidate integrity mismatches and missing candidate artifacts with actionable failure state', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const worktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t070000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t070000z', worktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);