artsWith('--resume=')) {
    const runId = first.slice('--resume='.length).trim();
    if (!runId) {
      throw new Error(`--resume requires <run-id>.\n${AUTORESEARCH_HELP}`);
    }
    return { missionDir: null, runId, codexArgs: values.slice(1) };
  }
  if (first === 'run') {
    const missionDir = values[1]?.trim();
    if (!missionDir) {
      throw new Error(`run requires <mission-dir>.\n${AUTORESEARCH_HELP}`);
    }
    return { missionDir, runId: null, codexArgs: values.slice(2), runSubcommand: true };
  }
  if (first.startsWith('-')) {
    const seedArgs = parseInitArgs(values);
    return { missionDir: null, runId: null, codexArgs: [], guided: true, seedArgs };
  }
  return { missionDir: first, runId: null, codexArgs: values.slice(1) };
}