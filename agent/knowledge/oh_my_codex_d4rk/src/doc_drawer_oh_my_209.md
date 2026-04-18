ass');
      assert.equal(latestEvaluator.pass, true);
      assert.equal(latestEvaluator.score, 1);

      const results = await readFile(runtime.resultsFile, 'utf-8');
      assert.match(results, /^iteration	commit	pass	score	status	description$/m);
      assert.match(results, /^0	.+	true	1	baseline	initial baseline evaluation$/m);

      const state = await readModeState('autoresearch', repo);
      assert.ok(state);