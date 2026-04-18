ve: true });
      await writeFile(join(missionDir, 'mission.md'), '# Mission\nShip it\n', 'utf-8');

      await assert.rejects(
        () => loadAutoresearchMissionContract(missionDir),
        /sandbox\.md is required inside mission-dir/i,
      );
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('loads mission contract from in-repo mission directory', async () => {
    const repo = await initRepo();
    try {
      const missionDir = join(repo, 'missions', 'demo');
      await mkdir(missionDir, { recursive: true });
      await writeFile(join(missionDir, 'mission.md'), '# Mission\nShip it\n', 'utf-8');
      await writeFile(
        join(missionDir, 'sandbox.md'),