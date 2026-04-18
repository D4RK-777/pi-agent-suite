Error(`Invalid ${flag} value "${value}". Expected a non-negative integer.`);
  }
  return parsed;
}

export function parseSessionSearchArgs(args: string[]): ParsedSessionSearchArgs {
  const options: SessionSearchOptions = {
    query: '',
  };
  let json = false;
  const queryTokens: string[] = [];

  for (let index = 0; index < args.length; index += 1) {
    const token = args[index];
    if (token === '--json') {
      json = true;
      continue;
    }
    if (token === '--case-sensitive') {
      options.caseSensitive = true;
      continue;
    }
    if (token === '--limit' || token === '--session' || token === '--since' || token === '--project' || token === '--context') {
      const next = args[index + 1];
      if (!next || next.startsWith('-')) {