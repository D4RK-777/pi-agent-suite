wd: worktreePath, encoding: 'utf-8' }).trim();
      assert.equal(headAfterDiscard, improvedCommit);

      const finalManifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      const results = await readFile(runtime.resultsFile, 'utf-8');
      assert.match(results, /^1\t.+\ttrue\t2\tkeep\timproved score$/m);
      assert.match(results, /^2\t.+\ttrue\t1\tdiscard\tworse score$/m);

      const ledger = JSON.parse(await readFile(runtime.ledgerFile, 'utf-8')) as {
        entries: Array<{ decision: string; description: string }>;
      };
      assert.equal(ledger.entries.length, 3);
      assert.deepEqual(
        ledger.entries.map((entry) => [entry.decision, entry.description]),
        [
          ['baseline', 'initial baseline evaluation'],