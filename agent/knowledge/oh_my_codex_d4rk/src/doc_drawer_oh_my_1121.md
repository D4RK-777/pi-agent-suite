);
    assert.equal(result.keepPolicy, 'pass_only');
    assert.equal(result.slug, 'my-slug');
  });

  it('parses all flags with = syntax', () => {
    const result = parseInitArgs([
      '--topic=my topic',
      '--evaluator=node eval.js',
      '--keep-policy=score_improvement',
      '--slug=my-slug',
    ]);
    assert.equal(result.topic, 'my topic');
    assert.equal(result.evaluatorCommand, 'node eval.js');
    assert.equal(result.keepPolicy, 'score_improvement');
    assert.equal(result.slug, 'my-slug');
  });