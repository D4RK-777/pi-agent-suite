. Use <mission-dir> or init --topic/--evaluator/--keep-policy/--slug for non-interactive use.');
  }

  let topic = seedInputs.topic?.trim() || '';
  let evaluatorCommand = seedInputs.evaluatorCommand?.trim() || '';
  let keepPolicy: AutoresearchKeepPolicy = seedInputs.keepPolicy || 'score_improvement';
  let slug = seedInputs.slug?.trim() || '';

  try {
    while (true) {
      topic = await promptWithDefault(io, 'Research topic/goal', topic);
      if (!topic) {
        throw new Error('Research topic is required.');
      }