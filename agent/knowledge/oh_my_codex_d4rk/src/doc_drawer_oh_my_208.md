t.results_file, runtime.resultsFile);
      assert.equal(typeof manifest.baseline_commit, 'string');

      const ledger = JSON.parse(await readFile(runtime.ledgerFile, 'utf-8')) as Record<string, unknown>;
      assert.equal(Array.isArray(ledger.entries), true);
      assert.equal((ledger.entries as unknown[]).length, 1);

      const latestEvaluator = JSON.parse(await readFile(runtime.latestEvaluatorFile, 'utf-8')) as Record<string, unknown>;
      assert.equal(latestEvaluator.status, 'pass');
      assert.equal(latestEvaluator.pass, true);
      assert.equal(latestEvaluator.score, 1);