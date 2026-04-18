;
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'abort');

      const results = await readFile(runtime.resultsFile, 'utf-8');
      assert.match(results, /^1\t.+\t\t\tnoop\tno useful change$/m);
      assert.match(results, /^2\t.+\t\t\tabort\toperator stop$/m);

      const finalManifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      assert.equal(finalManifest.status, 'stopped');
      assert.equal(finalManifest.stop_reason, 'candidate abort');
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });