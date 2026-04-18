teFile, `${JSON.stringify({
        status: 'candidate',
        candidate_commit: parseErrorCommit,
        base_commit: manifest.last_kept_commit,
        description: 'parse error branch',
        notes: ['invalid json'],
        created_at: '2026-03-14T08:03:00.000Z',
      }, null, 2)}\n`, 'utf-8');
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'discard');

      const results = await readFile(runtime.resultsFile, 'utf-8');
      assert.match(results, /^1\t.+\t\t\tinterrupted\tclean interrupt$/m);
      assert.match(results, /^2\t.+\tfalse\t0\tdiscard\tfailing evaluator branch$/m);
      assert.match(results, /^3\t.+\t\t\tdiscard\tparse error branch$/m);