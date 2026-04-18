unId);
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'candidate',
        candidate_commit: improvedCommit,
        base_commit: initialManifest.last_kept_commit,
        description: 'improved score',
        notes: ['score raised to 2'],
        created_at: '2026-03-14T01:00:00.000Z',
      }, null, 2)}\n`, 'utf-8');

      const keepDecision = await processAutoresearchCandidate(worktreeContract, initialManifest, repo);
      assert.equal(keepDecision, 'keep');
      const keptManifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      assert.equal(keptManifest.last_kept_commit, improvedCommit);