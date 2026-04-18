},
      body: 'Stay inside the mission boundary.',
    },
    missionSlug: 'missions-demo',
  };
}

describe('autoresearch runtime parity extras', () => {
  it('treats allowed runtime files as reset-safe and blocks unrelated dirt', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const worktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t020000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t020000z', worktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);