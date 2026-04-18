mo/20260314t060000z', worktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });
      const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);
      const runtime = await prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T060000Z' });

      let manifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'noop',
        candidate_commit: null,
        base_commit: manifest.last_kept_commit,
        description: 'no useful change',
        notes: ['noop branch'],
        created_at: '2026-03-14T06:01:00.000Z',
      }, null, 2)}\n`, 'utf-8');