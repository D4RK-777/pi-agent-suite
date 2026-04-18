cy: pass_only/);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('uses seeded novice inputs while still requiring confirmation-driven launch', async () => {
    const repo = await initRepo();
    try {
      const result = await withMockedTty(() => runAutoresearchNoviceBridge(
        repo,
        {
          topic: 'Seeded topic',
          evaluatorCommand: 'node scripts/eval.js',
          keepPolicy: 'score_improvement',
          slug: 'seeded-topic',
        },
        makeFakeIo([
          '',
          '',
          '',
          '',
          '',
          'launch',
        ]),
      ));