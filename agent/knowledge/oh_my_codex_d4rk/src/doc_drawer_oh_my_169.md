const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);
      const runtime = await prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T020000Z' });

      await writeFile(join(worktreePath, 'results.tsv'), 'iteration\tcommit\tpass\tscore\tstatus\tdescription\n', 'utf-8');
      await writeFile(join(worktreePath, 'run.log'), 'ok\n', 'utf-8');
      assert.doesNotThrow(() => assertResetSafeWorktree(worktreePath));

      await writeFile(join(worktreePath, 'scratch.tmp'), 'nope\n', 'utf-8');
      assert.throws(() => assertResetSafeWorktree(worktreePath), /autoresearch_reset_requires_clean_worktree/i);