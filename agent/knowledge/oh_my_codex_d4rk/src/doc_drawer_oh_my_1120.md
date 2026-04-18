s/,
      );
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});

describe('parseInitArgs', () => {
  it('parses all flags with space-separated values', () => {
    const result = parseInitArgs([
      '--topic', 'my topic',
      '--evaluator', 'node eval.js',
      '--keep-policy', 'pass_only',
      '--slug', 'my-slug',
    ]);
    assert.equal(result.topic, 'my topic');
    assert.equal(result.evaluatorCommand, 'node eval.js');
    assert.equal(result.keepPolicy, 'pass_only');
    assert.equal(result.slug, 'my-slug');
  });