');
      assert.equal(await processAutoresearchCandidate(secondContract, manifest, repo), 'error');

      failedManifest = await loadAutoresearchRunManifest(repo, secondRuntime.runId);
      assert.equal(failedManifest.status, 'failed');
      assert.match(failedManifest.stop_reason || '', /base_commit/i);

      const thirdWorktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t072000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t072000z', thirdWorktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const thirdContract = await materializeAutoresearchMissionToWorktree(contract, thirdWorktreePath);