assert.equal(resumed.runId, runtime.runId);
      assert.equal(resumed.worktreePath, worktreePath);

      await writeFile(statePath, `${JSON.stringify(idleState, null, 2)}\n`, 'utf-8');
      await rm(worktreePath, { recursive: true, force: true });
      await assert.rejects(
        () => resumeAutoresearchRuntime(repo, runtime.runId),
        /autoresearch_resume_missing_worktree/i,
      );
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('decides ambiguous vs keep based on keep_policy semantics', () => {
    const candidate = {
      status: 'candidate' as const,
      candidate_commit: 'abc1234',
      base_commit: 'base1234',
      description: 'candidate',
      notes: [],
      created_at: '2026-03-14T05:00:00.000Z',
    };