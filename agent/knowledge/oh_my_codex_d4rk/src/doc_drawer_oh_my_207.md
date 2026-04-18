th, 'node_modules')), true);
      assert.doesNotThrow(() => assertResetSafeWorktree(worktreePath));

      const manifest = JSON.parse(await readFile(runtime.manifestFile, 'utf-8')) as Record<string, unknown>;
      assert.equal(manifest.mission_slug, 'missions-demo');
      assert.equal(manifest.branch_name, 'autoresearch/missions-demo/20260314t000000z');
      assert.equal(manifest.mission_dir, join(worktreePath, 'missions', 'demo'));
      assert.equal(manifest.worktree_path, worktreePath);
      assert.equal(manifest.results_file, runtime.resultsFile);
      assert.equal(typeof manifest.baseline_commit, 'string');