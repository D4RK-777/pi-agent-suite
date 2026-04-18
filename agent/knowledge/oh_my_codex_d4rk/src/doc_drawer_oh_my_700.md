if (token.startsWith('--session=')) {
      options.session = token.slice('--session='.length);
      continue;
    }
    if (token.startsWith('--since=')) {
      options.since = token.slice('--since='.length);
      continue;
    }
    if (token.startsWith('--project=')) {
      options.project = token.slice('--project='.length);
      continue;
    }
    if (token.startsWith('--context=')) {
      options.context = parsePositiveInteger(token.slice('--context='.length), '--context');
      continue;
    }
    if (token.startsWith('-')) {
      throw new Error(`Unknown option: ${token}`);
    }
    queryTokens.push(token);
  }

  options.query = queryTokens.join(' ').trim();
  if (options.query === '') {
    throw new Error(`Missing search query.\n${HELP}`);
  }