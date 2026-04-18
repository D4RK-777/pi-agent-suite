it prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T050000Z' });
      const manifest = JSON.parse(await readFile(runtime.manifestFile, 'utf-8')) as Record<string, unknown>;
      manifest.status = 'completed';
      await writeFile(runtime.manifestFile, `${JSON.stringify(manifest, null, 2)}\n`, 'utf-8');
      await writeFile(join(repo, '.omx', 'state', 'autoresearch-state.json'), `${JSON.stringify({
        schema_version: 1,
        active: false,
        run_id: runtime.runId,
        mission_slug: contract.missionSlug,
        repo_root: repo,
        worktree_path: worktreePath,
        status: 'completed',
        updated_at: '2026-03-14T05:05:00.000Z',
      }, null, 2)}\n`, 'utf-8');