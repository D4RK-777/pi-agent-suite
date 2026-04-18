const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);
      const runtime = await prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T070000Z' });

      let manifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'candidate',
        candidate_commit: null,
        base_commit: manifest.last_kept_commit,
        description: 'invalid candidate',
        notes: ['missing commit'],
        created_at: '2026-03-14T07:01:00.000Z',
      }, null, 2)}\n`, 'utf-8');
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'error');