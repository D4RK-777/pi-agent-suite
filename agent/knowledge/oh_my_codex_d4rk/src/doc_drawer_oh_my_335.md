in(missionDir, 'sandbox.md'), sandboxContent, 'utf-8');

  return { missionDir, slug: opts.slug };
}

export function parseInitArgs(args: readonly string[]): Partial<InitAutoresearchOptions> {
  const result: Partial<InitAutoresearchOptions> = {};
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    const next = args[i + 1];
    if ((arg === '--topic') && next) {
      result.topic = next;
      i++;
    } else if ((arg === '--evaluator') && next) {
      result.evaluatorCommand = next;
      i++;
    } else if ((arg === '--keep-policy') && next) {
      const normalized = next.trim().toLowerCase();
      if (normalized !== 'pass_only' && normalized !== 'score_improvement') {
        throw new Error('--keep-policy must be one of: score_improvement, pass_only');
      }