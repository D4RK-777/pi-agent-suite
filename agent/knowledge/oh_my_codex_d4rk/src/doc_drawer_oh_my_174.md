it prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T040000Z' });
      const statePath = join(repo, '.omx', 'state', 'autoresearch-state.json');
      const idleState = {
        schema_version: 1,
        active: false,
        run_id: runtime.runId,
        mission_slug: contract.missionSlug,
        repo_root: repo,
        worktree_path: worktreePath,
        status: 'idle',
        updated_at: '2026-03-14T04:05:00.000Z',
      };
      await writeFile(statePath, `${JSON.stringify(idleState, null, 2)}\n`, 'utf-8');

      const resumed = await resumeAutoresearchRuntime(repo, runtime.runId);
      assert.equal(resumed.runId, runtime.runId);
      assert.equal(resumed.worktreePath, worktreePath);