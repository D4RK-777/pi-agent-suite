> parseEvaluatorResult('{"pass":true,"score":"high"}'),
      /score must be numeric/i,
    );
  });

  it('rejects mission directories outside a git repository', async () => {
    const missionDir = await mkdtemp(join(tmpdir(), 'omx-autoresearch-not-git-'));
    try {
      await writeFile(join(missionDir, 'mission.md'), '# Mission\nShip it\n', 'utf-8');
      await writeFile(
        join(missionDir, 'sandbox.md'),
        `---\nevaluator:\n  command: node scripts/eval.js\n  format: json\n---\nStay in bounds.\n`,
        'utf-8',
      );