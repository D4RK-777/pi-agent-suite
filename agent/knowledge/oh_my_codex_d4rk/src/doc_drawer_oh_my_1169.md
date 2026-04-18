ursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });

  it('falls back to foreground execution when tmux split-window fails', async () => {
    const repo = await initRepo();
    const fakeBin = await mkdtemp(join(tmpdir(), 'omx-autoresearch-run-fallback-bin-'));
    try {
      const missionDir = join(repo, 'missions', 'demo');
      await mkdir(missionDir, { recursive: true });
      await mkdir(join(repo, 'scripts'), { recursive: true });
      await writeFile(join(missionDir, 'mission.md'), '# Mission\nFallback launch.\n', 'utf-8');
      await writeFile(
        join(missionDir, 'sandbox.md'),
        '---\nevaluator:\n  command: node scripts/eval.js\n  format: json\n  keep_policy: pass_only\n---\nStay inside the mission boundary.\n',