RED_ERROR);
  }
  if (format !== 'json') {
    throw contractError(EVALUATOR_FORMAT_JSON_ERROR);
  }

  return {
    frontmatter: parsedFrontmatter,
    evaluator: {
      command,
      format: 'json',
      ...(keepPolicy ? { keep_policy: keepPolicy } : {}),
    },
    body,
  };
}

export function parseEvaluatorResult(raw: string): AutoresearchEvaluatorResult {
  let parsed: unknown;
  try {
    parsed = JSON.parse(raw);
  } catch {
    throw contractError('Evaluator output must be valid JSON with required boolean pass and optional numeric score.');
  }

  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
    throw contractError('Evaluator output must be a JSON object.');
  }