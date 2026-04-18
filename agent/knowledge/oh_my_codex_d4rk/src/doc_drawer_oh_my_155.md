sert.equal(parsed.evaluator.format, 'json');
    assert.equal(parsed.body, 'Stay in bounds.');
  });

  it('rejects sandbox contract without frontmatter', () => {
    assert.throws(
      () => parseSandboxContract('No frontmatter here'),
      /sandbox\.md must start with YAML frontmatter/i,
    );
  });

  it('rejects sandbox contract without evaluator command', () => {
    assert.throws(
      () => parseSandboxContract(`---\nevaluator:\n  format: json\n---\nPolicy\n`),
      /evaluator\.command is required/i,
    );
  });

  it('rejects sandbox contract without evaluator format', () => {
    assert.throws(
      () => parseSandboxContract(`---\nevaluator:\n  command: node eval.js\n---\nPolicy\n`),
      /evaluator\.format is required/i,
    );
  });