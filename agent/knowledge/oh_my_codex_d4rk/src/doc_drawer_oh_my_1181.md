.match(`${result.stderr}\n${result.stdout}`, /Cannot start autoresearch: ralph is already active/i);

      const worktreesRoot = join(repo, '.omx', 'worktrees');
      assert.equal(existsSync(worktreesRoot), false, 'expected launch to abort before creating autoresearch worktree');
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('launches codex exec for autoresearch turns without shelling out to cat', async () => {
    const repo = await initRepo();
    const fakeBin = await mkdtemp(join(tmpdir(), 'omx-autoresearch-fake-bin-'));
    try {
      const missionDir = join(repo, 'missions', 'demo');
      await mkdir(missionDir, { recursive: true });
      await mkdir(join(repo, 'scripts'), { recursive: true });