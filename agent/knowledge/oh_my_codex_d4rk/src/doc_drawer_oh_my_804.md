value;
      continue;
    }
    if (token === '--tail-lines') {
      const next = args[index + 1];
      if (!next || next.startsWith('-')) throw new Error(`--tail-lines requires a numeric value.\n${SPARKSHELL_USAGE}`);
      const parsed = Number.parseInt(next, 10);
      if (!Number.isFinite(parsed) || parsed < 100 || parsed > 1000) {
        throw new Error(`--tail-lines must be an integer between 100 and 1000.\n${SPARKSHELL_USAGE}`);
      }
      tailLines = parsed;
      sawTailLines = true;
      index += 1;
      continue;
    }
    if (token.startsWith('--tail-lines=')) {
      const parsed = Number.parseInt(token.slice('--tail-lines='.length), 10);
      if (!Number.isFinite(parsed) || parsed < 100 || parsed > 1000) {