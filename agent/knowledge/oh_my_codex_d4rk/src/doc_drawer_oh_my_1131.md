d: 'node scripts/eval.js',
      keepPolicy: 'score_improvement',
      slug: 'flaky-tests',
    });

    assert.match(prompt, /\$deep-interview --autoresearch/);
    assert.match(prompt, /deep-interview-autoresearch-\{slug\}\.md/);
    assert.match(prompt, /autoresearch-\{slug\}\/mission\.md/);
    assert.match(prompt, /- topic: Investigate flaky tests/);
    assert.match(prompt, /- evaluator: node scripts\/eval\.js/);
    assert.match(prompt, /- keep_policy: score_improvement/);
    assert.match(prompt, /- slug: flaky-tests/);
  });
});