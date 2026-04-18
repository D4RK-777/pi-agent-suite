g behavior/);
      assert.match(sandboxContent, /command: node scripts\/eval\.js/);
    } finally {
      await rm(repo, { recursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });

  it('uses split-window launch for explicit run inside tmux while preserving the interview pane', async () => {
    const repo = await initRepo();
    const fakeBin = await mkdtemp(join(tmpdir(), 'omx-autoresearch-run-split-bin-'));
    try {
      const missionDir = join(repo, 'missions', 'demo');
      const tmuxLog = join(repo, 'tmux.log');
      await mkdir(missionDir, { recursive: true });
      await mkdir(join(repo, 'scripts'), { recursive: true });
      await writeFile(join(missionDir, 'mission.md'), '# Mission\nSplit pane launch.\n', 'utf-8');