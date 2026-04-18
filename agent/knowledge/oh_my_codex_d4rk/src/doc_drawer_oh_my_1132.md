mpt, /- keep_policy: score_improvement/);
    assert.match(prompt, /- slug: flaky-tests/);
  });
});

describe('runAutoresearchNoviceBridge', () => {
  it('loops through refine further before launching and writes draft + mission files', async () => {
    const repo = await initRepo();
    try {
      const result = await withMockedTty(() => runAutoresearchNoviceBridge(
        repo,
        {},
        makeFakeIo([
          'Improve evaluator UX',
          'Make success measurable',
          'TODO replace with evaluator command',
          'score_improvement',
          'ux-eval',
          'refine further',
          'Improve evaluator UX',
          'Passing evaluator output',
          'node scripts/eval.js',
          'pass_only',
          'ux-eval',
          'launch',