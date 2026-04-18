w !== 'object' || Array.isArray(evaluatorRaw)) {
    throw contractError(EVALUATOR_BLOCK_ERROR);
  }

  const evaluator = evaluatorRaw as { command?: unknown; format?: unknown; keep_policy?: unknown };
  const command = typeof evaluator.command === 'string'
    ? evaluator.command.trim()
    : '';
  const format = typeof evaluator.format === 'string'
    ? evaluator.format.trim().toLowerCase()
    : '';
  const keepPolicy = parseKeepPolicy(evaluator.keep_policy);

  if (!command) {
    throw contractError(EVALUATOR_COMMAND_ERROR);
  }
  if (!format) {
    throw contractError(EVALUATOR_FORMAT_REQUIRED_ERROR);
  }
  if (format !== 'json') {
    throw contractError(EVALUATOR_FORMAT_JSON_ERROR);
  }