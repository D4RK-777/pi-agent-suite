er|evaluator/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('rejects autoresearch launch when root ralph mode is already active', async () => {
    const repo = await initRepo();
    try {
      const missionDir = join(repo, 'missions', 'demo');
      await mkdir(missionDir, { recursive: true });
      await writeFile(join(missionDir, 'mission.md'), '# Mission\n', 'utf-8');
      await writeFile(
        join(missionDir, 'sandbox.md'),
        '---\nevaluator:\n  command: node eval.js\n  format: json\n---\nStay inside the mission boundary.\n',
        'utf-8',
      );
      await mkdir(join(repo, '.omx', 'state'), { recursive: true });
      await writeFile(
        join(repo, '.omx', 'state', 'ralph-state.json'),
        JSON.stringify({