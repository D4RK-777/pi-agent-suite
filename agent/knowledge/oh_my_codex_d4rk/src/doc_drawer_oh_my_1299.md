olveExploreSparkShellRoute('map the relationship between hooks and tmux helpers'), undefined);
  });

  it('routes qualifying read-only git commands to sparkshell', () => {
    assert.deepEqual(resolveExploreSparkShellRoute('git log --oneline'), {
      argv: ['git', 'log', '--oneline'],
      reason: 'long-output',
    });
    assert.deepEqual(resolveExploreSparkShellRoute('run git diff --stat'), {
      argv: ['git', 'diff', '--stat'],
      reason: 'long-output',
    });
  });