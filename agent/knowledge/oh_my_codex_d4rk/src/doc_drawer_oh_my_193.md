ePath, encoding: 'utf-8' }).trim();
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'candidate',
        candidate_commit: failingCommit,
        base_commit: manifest.last_kept_commit,
        description: 'failing evaluator branch',
        notes: ['pass false'],
        created_at: '2026-03-14T08:02:00.000Z',
      }, null, 2)}\n`, 'utf-8');
      assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'discard');