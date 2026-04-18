n  command: node scripts/eval.js\n  format: json\n---\nStay in bounds.\n`,
        'utf-8',
      );

      await assert.rejects(
        () => loadAutoresearchMissionContract(missionDir),
        /not a git repository|mission-dir must be inside a git repository/i,
      );
    } finally {
      await rm(missionDir, { recursive: true, force: true });
    }
  });

  it('rejects mission directories missing sandbox.md', async () => {
    const repo = await initRepo();
    try {
      const missionDir = join(repo, 'missions', 'demo');
      await mkdir(missionDir, { recursive: true });
      await writeFile(join(missionDir, 'mission.md'), '# Mission\nShip it\n', 'utf-8');