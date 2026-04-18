const worktreeContractB = await materializeAutoresearchMissionToWorktree(contract, worktreePathB);

      await assert.rejects(
        () => prepareAutoresearchRuntime(worktreeContractB, repo, worktreePathB, { runTag: '20260314T030500Z' }),
        /autoresearch_active_run_exists/i,
      );
      assert.equal(existsSync(runtimeA.manifestFile), true);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });