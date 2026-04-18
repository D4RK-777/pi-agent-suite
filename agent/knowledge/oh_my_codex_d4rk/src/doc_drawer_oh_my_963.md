atch[0] ?? '').trim().toLowerCase();
    if (value) matches.add(value);
  }
  return matches.size;
}

function hasAtomicParallelizationSignals(task: string, size: ReturnType<typeof classifyTaskSize>['size']): boolean {
  const fileRefCount = countDistinctMatches(task, FILE_REFERENCE_PATTERN);
  const symbolRefCount = countDistinctMatches(task, CODE_SYMBOL_PATTERN);
  if (fileRefCount >= 2) return true;
  if (fileRefCount >= 1 && symbolRefCount >= 1) return true;
  if (PARALLELIZATION_SIGNAL.test(task) && size === 'large') return true;
  return size === 'large' && countWords(task) >= 24;
}