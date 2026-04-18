', '-b', 'autoresearch/missions-demo/20260314t030000z', worktreePathA, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContractA = await materializeAutoresearchMissionToWorktree(contract, worktreePathA);
      const runtimeA = await prepareAutoresearchRuntime(worktreeContractA, repo, worktreePathA, { runTag: '20260314T030000Z' });

      const worktreePathB = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t030500z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t030500z', worktreePathB, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContractB = await materializeAutoresearchMissionToWorktree(contract, worktreePathB);