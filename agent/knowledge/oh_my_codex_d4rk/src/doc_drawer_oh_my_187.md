repareAutoresearchRuntime(secondContract, repo, secondWorktreePath, { runTag: '20260314T071000Z' });

      manifest = await loadAutoresearchRunManifest(repo, secondRuntime.runId);
      await writeFile(secondRuntime.candidateFile, `${JSON.stringify({
        status: 'candidate',
        candidate_commit: manifest.last_kept_commit,
        base_commit: 'deadbeef',
        description: 'mismatched base',
        notes: ['bad base'],
        created_at: '2026-03-14T07:02:00.000Z',
      }, null, 2)}\n`, 'utf-8');
      assert.equal(await processAutoresearchCandidate(secondContract, manifest, repo), 'error');