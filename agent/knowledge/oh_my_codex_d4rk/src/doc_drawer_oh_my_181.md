s: ['noop branch'],
        created_at: '2026-03-14T06:01:00.000Z',
      }, null, 2)}\n`, 'utf-8');
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'noop');

      manifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'abort',
        candidate_commit: null,
        base_commit: manifest.last_kept_commit,
        description: 'operator stop',
        notes: ['abort branch'],
        created_at: '2026-03-14T06:02:00.000Z',
      }, null, 2)}\n`, 'utf-8');
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'abort');