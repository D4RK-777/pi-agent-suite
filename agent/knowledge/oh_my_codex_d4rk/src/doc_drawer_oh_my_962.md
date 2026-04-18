rallel|separately|verification|verify|tests?|docs?|documentation|benchmarks?|migration|rollout)\b/i;

function countWords(text: string): number {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

function countDistinctMatches(text: string, pattern: RegExp): number {
  const matches = new Set<string>();
  for (const match of text.matchAll(new RegExp(pattern.source, pattern.flags.includes('g') ? pattern.flags : `${pattern.flags}g`))) {
    const value = (match[1] ?? match[0] ?? '').trim().toLowerCase();
    if (value) matches.add(value);
  }
  return matches.size;
}