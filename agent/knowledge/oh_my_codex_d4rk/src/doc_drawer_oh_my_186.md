resultsFile, 'utf-8');
      assert.match(failureResults, /^1\t.+\t\t\terror\tinvalid candidate$/m);

      const secondWorktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t071000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t071000z', secondWorktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const secondContract = await materializeAutoresearchMissionToWorktree(contract, secondWorktreePath);
      const secondRuntime = await prepareAutoresearchRuntime(secondContract, repo, secondWorktreePath, { runTag: '20260314T071000Z' });