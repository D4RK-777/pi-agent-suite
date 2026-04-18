blished/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});


describe('autoresearch parity decisions', () => {
  it('keeps improved candidates and resets discarded candidates back to the last kept commit', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const worktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t010000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t010000z', worktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);