keepPolicy: 'score_improvement',
        slug: 'flaky-tests',
        repoRoot: repo,
      });

      const sandboxContent = await readFile(join(result.missionDir, 'sandbox.md'), 'utf-8');
      const parsed = parseSandboxContract(sandboxContent);
      assert.equal(parsed.evaluator.command, 'bash run-tests.sh');
      assert.equal(parsed.evaluator.format, 'json');
      assert.equal(parsed.evaluator.keep_policy, 'score_improvement');
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('throws if mission directory already exists', async () => {
    const repo = await initRepo();
    try {
      const missionDir = join(repo, 'missions', 'existing');
      await mkdir(missionDir, { recursive: true });