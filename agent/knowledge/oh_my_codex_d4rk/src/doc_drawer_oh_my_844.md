EAM_API_OPERATIONS.join(', ')}`);
  }
  let input: Record<string, unknown> = {};
  let json = false;
  for (let i = 1; i < args.length; i += 1) {
    const token = args[i];
    if (token === '--json') {
      json = true;
      continue;
    }
    if (token === '--input') {
      const next = args[i + 1];
      if (!next) throw new Error('Missing value after --input');
      try {
        const parsed = JSON.parse(next) as unknown;
        if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
          throw new Error('input must be a JSON object');
        }
        input = parsed as Record<string, unknown>;
      } catch (error) {
        throw new Error(`Invalid --input JSON: ${error instanceof Error ? error.message : String(error)}`);
      }
      i += 1;