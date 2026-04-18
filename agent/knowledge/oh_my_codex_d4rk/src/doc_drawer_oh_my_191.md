const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);
      const runtime = await prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T080000Z' });

      let manifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'interrupted',
        candidate_commit: null,
        base_commit: manifest.last_kept_commit,
        description: 'clean interrupt',
        notes: ['ctrl-c'],
        created_at: '2026-03-14T08:01:00.000Z',
      }, null, 2)}\n`, 'utf-8');
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'interrupted');