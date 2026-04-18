en === '--context') {
      const next = args[index + 1];
      if (!next || next.startsWith('-')) {
        throw new Error(`Missing value after ${token}.`);
      }
      if (token === '--limit') options.limit = parsePositiveInteger(next, token);
      if (token === '--session') options.session = next;
      if (token === '--since') options.since = next;
      if (token === '--project') options.project = next;
      if (token === '--context') options.context = parsePositiveInteger(next, token);
      index += 1;
      continue;
    }
    if (token.startsWith('--limit=')) {
      options.limit = parsePositiveInteger(token.slice('--limit='.length), '--limit');
      continue;
    }
    if (token.startsWith('--session=')) {
      options.session = token.slice('--session='.length);