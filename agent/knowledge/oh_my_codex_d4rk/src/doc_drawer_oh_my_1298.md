'--model-spark',
      'spark-model',
      '--model-fallback',
      'gpt-5.4',
    ]);
  });
});

describe('resolveExploreSparkShellRoute', () => {
  it('keeps natural-language exploration prompts on the direct harness path', () => {
    assert.equal(resolveExploreSparkShellRoute('which files define team routing'), undefined);
    assert.equal(resolveExploreSparkShellRoute('map the relationship between hooks and tmux helpers'), undefined);
  });