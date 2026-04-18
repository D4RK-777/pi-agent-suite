=> {
    const result = checkTmuxAvailable();
    assert.equal(typeof result, 'boolean');
  });
});

describe('autoresearch intake draft artifacts', () => {
  it('writes a canonical deep-interview autoresearch draft artifact from vague input', async () => {
    const repo = await initRepo();
    try {
      const artifact = await writeAutoresearchDraftArtifact({
        repoRoot: repo,
        topic: 'Improve onboarding for first-time contributors',
        keepPolicy: 'score_improvement',
        seedInputs: { topic: 'Improve onboarding for first-time contributors' },
      });