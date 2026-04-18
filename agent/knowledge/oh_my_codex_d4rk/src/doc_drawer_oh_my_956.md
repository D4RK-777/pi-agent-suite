plan.strategy === 'numbered' || plan.strategy === 'bulleted') {
    return requestedWorkerCount;
  }

  const size = classifyTaskSize(task).size;
  if (plan.strategy === 'atomic') {
    if (looksLikeLowConfidenceAnalysisTask(task)) {
      return 1;
    }

    if (size === 'small') {
      const proseHeavyAtomicTask = countWords(task) > 18 || CONTEXTUAL_DECOMPOSITION_CLAUSE.test(task);
      if (!proseHeavyAtomicTask) return 1;
    }

    if (!hasAtomicParallelizationSignals(task, size)) {
      return 1;
    }
  }

  if (plan.strategy === 'conjunction' && size !== 'large') {
    return Math.min(requestedWorkerCount, Math.max(2, plan.subtasks.length));
  }

  return requestedWorkerCount;
}