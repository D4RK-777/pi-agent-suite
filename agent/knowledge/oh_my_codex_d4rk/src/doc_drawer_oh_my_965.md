se;
  return parts.every((part) => countWords(part) <= 8 && looksLikeStandaloneWeakSubtask(part));
}

/** Split a task string into sub-tasks using numbered lists or conservative delimiters. */
function splitTaskString(task: string): DecompositionPlan {
  // Try numbered list: "1. foo 2. bar 3. baz" or "1) foo 2) bar"
  const numberedPattern = /(?:^|\s)(\d+)[.)]\s+/g;
  const numberedMatches = [...task.matchAll(numberedPattern)];
  if (numberedMatches.length >= 2) {
    const parts: Array<{ subject: string; description: string }> = [];
    for (let i = 0; i < numberedMatches.length; i++) {
      const prefixLen = numberedMatches[i][0].length;
      const contentStart = numberedMatches[i].index! + prefixLen;