it prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T000000Z' });

      assert.equal(existsSync(worktreeContract.missionFile), true);
      assert.equal(existsSync(worktreeContract.sandboxFile), true);
      assert.equal(existsSync(runtime.instructionsFile), true);
      assert.equal(existsSync(runtime.manifestFile), true);
      assert.equal(existsSync(runtime.ledgerFile), true);
      assert.equal(existsSync(runtime.latestEvaluatorFile), true);
      assert.equal(existsSync(runtime.resultsFile), true);
      assert.equal(existsSync(join(worktreePath, 'node_modules')), true);
      assert.doesNotThrow(() => assertResetSafeWorktree(worktreePath));