) => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const instructions = buildAutoresearchInstructions(contract, { runId: 'missions-demo-20260314t000000z', iteration: 1, baselineCommit: 'abc1234', lastKeptCommit: 'abc1234', resultsFile: 'results.tsv', candidateFile: '.omx/logs/autoresearch/missions-demo-20260314t000000z/candidate.json', keepPolicy: 'score_improvement' });
      assert.match(instructions, /exactly one experiment cycle/i);
      assert.match(instructions, /required output field: pass/i);
      assert.match(instructions, /optional output field: score/i);
      assert.match(instructions, /Iteration state snapshot:/i);
      assert.match(instructions, /Mission file:/i);
      assert.match(instructions, /Sandbox policy:/i);