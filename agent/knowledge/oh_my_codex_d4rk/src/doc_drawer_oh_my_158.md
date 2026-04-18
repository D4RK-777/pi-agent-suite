ss only', () => {
    assert.deepEqual(parseEvaluatorResult('{"pass":true}'), { pass: true });
  });

  it('accepts evaluator result with pass and score', () => {
    assert.deepEqual(parseEvaluatorResult('{"pass":false,"score":61}'), { pass: false, score: 61 });
  });

  it('rejects evaluator result without pass', () => {
    assert.throws(
      () => parseEvaluatorResult('{"score":61}'),
      /must include boolean pass/i,
    );
  });

  it('rejects evaluator result with non-numeric score', () => {
    assert.throws(
      () => parseEvaluatorResult('{"pass":true,"score":"high"}'),
      /score must be numeric/i,
    );
  });