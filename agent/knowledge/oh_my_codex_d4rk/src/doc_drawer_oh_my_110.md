ecisionReason: 'score improved over last kept score',
      keep: true,
      evaluator: evaluation,
      notes: ['candidate kept because evaluator score increased'],
    };
  }
  return {
    decision: 'discard',
    decisionReason: 'score did not improve',
    keep: false,
    evaluator: evaluation,
    notes: ['candidate discarded because evaluator score was not better than the kept baseline'],
  };
}