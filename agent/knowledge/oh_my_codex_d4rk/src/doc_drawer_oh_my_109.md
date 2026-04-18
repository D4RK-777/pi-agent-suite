'pass_only keep policy accepted evaluator pass=true',
      keep: true,
      evaluator: evaluation,
      notes: ['candidate kept because sandbox opted into pass_only policy'],
    };
  }
  if (!comparableScore(manifest.last_kept_score, evaluation.score)) {
    return {
      decision: 'ambiguous',
      decisionReason: 'evaluator pass without comparable score',
      keep: false,
      evaluator: evaluation,
      notes: ['candidate discarded because score_improvement policy requires comparable numeric scores'],
    };
  }
  if ((evaluation.score as number) > (manifest.last_kept_score as number)) {
    return {
      decision: 'keep',
      decisionReason: 'score improved over last kept score',
      keep: true,
      evaluator: evaluation,