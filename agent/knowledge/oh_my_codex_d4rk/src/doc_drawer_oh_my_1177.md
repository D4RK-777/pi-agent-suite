/sandbox\.md/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('rejects sandbox.md without evaluator frontmatter', async () => {
    const repo = await initRepo();
    try {
      const missionDir = join(repo, 'missions', 'demo');
      await mkdir(missionDir, { recursive: true });
      await writeFile(join(missionDir, 'mission.md'), '# Mission\n', 'utf-8');
      await writeFile(join(missionDir, 'sandbox.md'), 'No frontmatter here.\n', 'utf-8');