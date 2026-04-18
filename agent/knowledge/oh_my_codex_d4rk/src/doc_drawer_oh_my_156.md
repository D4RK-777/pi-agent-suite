tor:\n  command: node eval.js\n---\nPolicy\n`),
      /evaluator\.format is required/i,
    );
  });

  it('rejects sandbox contract with non-json evaluator format', () => {
    assert.throws(
      () => parseSandboxContract(`---\nevaluator:\n  command: node eval.js\n  format: text\n---\nPolicy\n`),
      /evaluator\.format must be json/i,
    );
  });

  it('normalizes evaluator keep_policy casing and surrounding whitespace', () => {
    const parsed = parseSandboxContract(`---
evaluator:
  command: node scripts/eval.js
  format: json
  keep_policy: "  SCORE_IMPROVEMENT  "
---
Stay in bounds.
`);
    assert.equal(parsed.evaluator.keep_policy, 'score_improvement');
  });