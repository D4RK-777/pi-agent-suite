al.js'), true);
    assert.equal(isLaunchReadyEvaluatorCommand('bash scripts/eval.sh'), true);
  });

  it('writes launch-consumable mission/sandbox/result artifacts and resolves them back', async () => {
    const repo = await initRepo();
    try {
      const artifacts = await writeAutoresearchDeepInterviewArtifacts({
        repoRoot: repo,
        topic: 'Measure onboarding friction',
        evaluatorCommand: 'node scripts/eval.js',
        keepPolicy: 'pass_only',
        slug: 'onboarding-friction',
        seedInputs: { topic: 'Measure onboarding friction' },
      });