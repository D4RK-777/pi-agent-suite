urn {
      decision: 'abort',
      decisionReason: 'candidate requested abort',
      keep: false,
      evaluator: null,
      notes: ['run stopped by candidate artifact'],
    };
  }
  if (candidate.status === 'noop') {
    return {
      decision: 'noop',
      decisionReason: 'candidate reported noop',
      keep: false,
      evaluator: null,
      notes: ['no code change was proposed'],
    };
  }
  if (candidate.status === 'interrupted') {
    return {
      decision: 'interrupted',
      decisionReason: 'candidate session was interrupted',
      keep: false,
      evaluator: null,
      notes: ['supervisor should inspect worktree cleanliness before continuing'],
    };
  }
  if (!evaluation || evaluation.status === 'error') {
    return {
      decision: 'discard',