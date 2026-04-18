luation$/m);

      const state = await readModeState('autoresearch', repo);
      assert.ok(state);

      const worktreeState = await readModeState('autoresearch', worktreePath);
      assert.equal(worktreeState, null);
      assert.equal(state?.active, true);
      assert.equal(state?.current_phase, 'running');
      assert.equal(state?.mission_slug, 'missions-demo');
      assert.equal(state?.mission_dir, join(worktreePath, 'missions', 'demo'));
      assert.equal(state?.worktree_path, worktreePath);
      assert.equal(state?.bootstrap_instructions_path, runtime.instructionsFile);
      assert.equal(state?.latest_evaluator_status, 'pass');
      assert.equal(state?.results_file, runtime.resultsFile);
      assert.equal(state?.baseline_commit, manifest.baseline_commit);