"
---
Stay in bounds.
`);
    assert.equal(parsed.evaluator.keep_policy, 'score_improvement');
  });

  it('parses optional evaluator keep_policy', () => {
    const parsed = parseSandboxContract(`---
evaluator:
  command: node scripts/eval.js
  format: json
  keep_policy: pass_only
---
Stay in bounds.
`);
    assert.equal(parsed.evaluator.keep_policy, 'pass_only');
  });

  it('rejects unsupported evaluator keep_policy', () => {
    assert.throws(
      () => parseSandboxContract(`---
evaluator:
  command: node scripts/eval.js
  format: json
  keep_policy: maybe
---
Stay in bounds.
`),
      /keep_policy must be one of/i,
    );
  });

  it('accepts evaluator result with pass only', () => {
    assert.deepEqual(parseEvaluatorResult('{"pass":true}'), { pass: true });
  });