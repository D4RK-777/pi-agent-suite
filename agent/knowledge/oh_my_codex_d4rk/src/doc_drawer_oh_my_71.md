|| Array.isArray(parsed)) {
    throw contractError('Evaluator output must be a JSON object.');
  }

  const result = parsed as Record<string, unknown>;
  if (typeof result.pass !== 'boolean') {
    throw contractError('Evaluator output must include boolean pass.');
  }
  if (result.score !== undefined && typeof result.score !== 'number') {
    throw contractError('Evaluator output score must be numeric when provided.');
  }

  return {
    pass: result.pass,
    ...(result.score === undefined ? {} : { score: result.score }),
  };
}