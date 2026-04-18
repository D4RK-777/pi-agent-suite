lid --input JSON: ${error instanceof Error ? error.message : String(error)}`);
      }
      i += 1;
      continue;
    }
    if (token.startsWith('--input=')) {
      const raw = token.slice('--input='.length);
      try {
        const parsed = JSON.parse(raw) as unknown;
        if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
          throw new Error('input must be a JSON object');
        }
        input = parsed as Record<string, unknown>;
      } catch (error) {
        throw new Error(`Invalid --input JSON: ${error instanceof Error ? error.message : String(error)}`);
      }
      continue;
    }
    throw new Error(`Unknown argument for "omx team api": ${token}`);
  }
  return { operation, input, json };
}