pInterviewDraftPaths(repoRoot));
  process.env[AUTORESEARCH_APPEND_INSTRUCTIONS_ENV] = appendixPath;

  try {
    const { launchWithHud } = await import('./index.js');
    await launchWithHud([buildAutoresearchDeepInterviewPrompt(seedArgs ?? {})]);
  } finally {
    if (typeof previousInstructionsFile === 'string') {
      process.env[AUTORESEARCH_APPEND_INSTRUCTIONS_ENV] = previousInstructionsFile;
    } else {
      delete process.env[AUTORESEARCH_APPEND_INSTRUCTIONS_ENV];
    }
  }