SEARCH_HELP}`);
    }
    return { missionDir: null, runId: null, codexArgs: [], guided: true };
  }

  const first = values[0];
  if (first === 'init') {
    return { missionDir: null, runId: null, codexArgs: [], guided: true, initArgs: values.slice(1) };
  }
  if (first === '--help' || first === '-h' || first === 'help') {
    return { missionDir: '--help', runId: null, codexArgs: [] };
  }
  if (first === '--resume') {
    const runId = values[1]?.trim();
    if (!runId) {
      throw new Error(`--resume requires <run-id>.\n${AUTORESEARCH_HELP}`);
    }
    return { missionDir: null, runId, codexArgs: values.slice(2) };
  }
  if (first.startsWith('--resume=')) {
    const runId = first.slice('--resume='.length).trim();
    if (!runId) {