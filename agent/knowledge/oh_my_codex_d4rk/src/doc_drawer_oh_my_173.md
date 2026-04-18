estFile), true);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('resumes a running manifest and rejects missing worktrees', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const worktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t040000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t040000z', worktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);
      const runtime = await prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T040000Z' });