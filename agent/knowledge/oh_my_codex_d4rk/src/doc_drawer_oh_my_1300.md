t diff --stat'), {
      argv: ['git', 'diff', '--stat'],
      reason: 'long-output',
    });
  });

  it('rejects non-read-only or shell-unsafe commands for sparkshell routing', () => {
    assert.equal(resolveExploreSparkShellRoute('git commit -m test'), undefined);
    assert.equal(resolveExploreSparkShellRoute('npm test'), undefined);
    assert.equal(resolveExploreSparkShellRoute('git log | head'), undefined);
    assert.equal(resolveExploreSparkShellRoute('find /tmp -maxdepth 1'), undefined);
  });
});