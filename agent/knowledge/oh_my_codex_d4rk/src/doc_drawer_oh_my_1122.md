ssert.equal(result.keepPolicy, 'score_improvement');
    assert.equal(result.slug, 'my-slug');
  });

  it('returns partial result when some flags are missing', () => {
    const result = parseInitArgs(['--topic', 'my topic']);
    assert.equal(result.topic, 'my topic');
    assert.equal(result.evaluatorCommand, undefined);
    assert.equal(result.keepPolicy, undefined);
    assert.equal(result.slug, undefined);
  });

  it('throws on invalid keep-policy', () => {
    assert.throws(
      () => parseInitArgs(['--keep-policy', 'invalid']),
      /must be one of/,
    );
  });

  it('throws on unknown flags', () => {
    assert.throws(
      () => parseInitArgs(['--unknown-flag', 'value']),
      /Unknown init flag: --unknown-flag/,
    );
  });