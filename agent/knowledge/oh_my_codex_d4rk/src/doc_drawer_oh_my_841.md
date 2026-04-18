_NOTES[operation]}\n`
    : '';

  return `
Usage: omx team api ${operation} --input <json> [--json]

Required input fields:
${required}${optional}${note}Example:
  omx team api ${operation} --input '${sampleInputJson}' --json
`.trim();
}

function buildJsonBase(): { schema_version: string; timestamp: string } {
  return {
    schema_version: '1.0',
    timestamp: new Date().toISOString(),
  };
}

function parseStatusTailLines(args: string[]): number {
  for (let index = 0; index < args.length; index += 1) {
    const token = args[index];
    if (token === '--tail-lines') {
      const next = args[index + 1];
      const parsed = Number.parseInt(next || '', 10);
      if (!Number.isFinite(parsed) || parsed < MIN_SPARKSHELL_TAIL_LINES || parsed > MAX_SPARKSHELL_TAIL_LINES) {