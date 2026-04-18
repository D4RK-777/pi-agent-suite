});
  const stdout = result.stdout?.trim() || '';
  const stderr = result.stderr?.trim() || '';

  let record: AutoresearchEvaluationRecord;
  if (result.error || result.status !== 0) {
    record = {
      command: contract.sandbox.evaluator.command,
      ran_at,
      status: 'error',
      exit_code: result.status,
      stdout,
      stderr: result.error ? [stderr, result.error.message].filter(Boolean).join('\n') : stderr,
    };
  } else {
    try {
      const parsed = parseEvaluatorResult(stdout);
      record = {
        command: contract.sandbox.evaluator.command,
        ran_at,
        status: parsed.pass ? 'pass' : 'fail',
        pass: parsed.pass,
        ...(parsed.score !== undefined ? { score: parsed.score } : {}),
        exit_code: result.status,
        stdout,