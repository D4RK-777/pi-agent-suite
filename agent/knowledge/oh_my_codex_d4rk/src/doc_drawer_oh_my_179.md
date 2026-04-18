tatus: 'completed',
        updated_at: '2026-03-14T05:05:00.000Z',
      }, null, 2)}\n`, 'utf-8');

      await assert.rejects(
        () => resumeAutoresearchRuntime(repo, runtime.runId),
        /autoresearch_resume_terminal_run/i,
      );
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('records noop and abort candidate branches explicitly', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);
      const worktreePath = join(repo, '.omx', 'worktrees', 'autoresearch-missions-demo-20260314t060000z');
      execFileSync('git', ['worktree', 'add', '-b', 'autoresearch/missions-demo/20260314t060000z', worktreePath, 'HEAD'], {
        cwd: repo,
        stdio: 'ignore',
      });