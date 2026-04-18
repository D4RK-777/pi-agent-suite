candidate_commit: worseCommit,
        base_commit: beforeDiscardManifest.last_kept_commit,
        description: 'worse score',
        notes: ['score dropped back to 1'],
        created_at: '2026-03-14T01:05:00.000Z',
      }, null, 2)}\n`, 'utf-8');

      const discardDecision = await processAutoresearchCandidate(worktreeContract, beforeDiscardManifest, repo);
      assert.equal(discardDecision, 'discard');
      const headAfterDiscard = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: worktreePath, encoding: 'utf-8' }).trim();
      assert.equal(headAfterDiscard, improvedCommit);