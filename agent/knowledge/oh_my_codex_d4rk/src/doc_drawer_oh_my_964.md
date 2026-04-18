.test(task) && size === 'large') return true;
  return size === 'large' && countWords(task) >= 24;
}

function looksLikeStandaloneWeakSubtask(part: string): boolean {
  const normalized = part.trim().replace(/^[*-]\s*/, '');
  return ACTIONABLE_TASK_PREFIX.test(normalized) || TASK_LABEL_PREFIX.test(normalized);
}

function canSafelySplitWeakTaskList(task: string, parts: string[]): boolean {
  if (parts.length < 2) return false;
  if (countWords(task) > 18) return false;
  if (CONTEXTUAL_DECOMPOSITION_CLAUSE.test(task)) return false;
  return parts.every((part) => countWords(part) <= 8 && looksLikeStandaloneWeakSubtask(part));
}