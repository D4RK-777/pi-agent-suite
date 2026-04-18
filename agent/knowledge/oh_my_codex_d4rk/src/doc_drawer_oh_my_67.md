;
      continue;
    }

    result[key] = value;
    currentSection = null;
  }

  return result;
}

function parseKeepPolicy(raw: unknown): AutoresearchKeepPolicy | undefined {
  if (raw === undefined) return undefined;
  if (typeof raw !== 'string') {
    throw contractError('sandbox.md frontmatter evaluator.keep_policy must be a string when provided.');
  }
  const normalized = raw.trim().toLowerCase();
  if (!normalized) return undefined;
  if (normalized === 'pass_only') return 'pass_only';
  if (normalized === 'score_improvement') return 'score_improvement';
  throw contractError('sandbox.md frontmatter evaluator.keep_policy must be one of: score_improvement, pass_only.');
}