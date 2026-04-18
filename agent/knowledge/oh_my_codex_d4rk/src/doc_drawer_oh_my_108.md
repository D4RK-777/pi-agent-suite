};
  }
  if (!evaluation || evaluation.status === 'error') {
    return {
      decision: 'discard',
      decisionReason: 'evaluator error',
      keep: false,
      evaluator: evaluation,
      notes: ['candidate discarded because evaluator errored or crashed'],
    };
  }
  if (!evaluation.pass) {
    return {
      decision: 'discard',
      decisionReason: 'evaluator reported failure',
      keep: false,
      evaluator: evaluation,
      notes: ['candidate discarded because evaluator pass=false'],
    };
  }
  if (manifest.keep_policy === 'pass_only') {
    return {
      decision: 'keep',
      decisionReason: 'pass_only keep policy accepted evaluator pass=true',
      keep: true,
      evaluator: evaluation,