;
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'error');

      let failedManifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      assert.equal(failedManifest.status, 'failed');
      assert.match(failedManifest.stop_reason || '', /non-null candidate_commit/i);

      const failureResults = await readFile(runtime.resultsFile, 'utf-8');
      assert.match(failureResults, /^1\t.+\t\t\terror\tinvalid candidate$/m);