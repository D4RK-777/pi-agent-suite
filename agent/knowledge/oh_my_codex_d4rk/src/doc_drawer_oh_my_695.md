xArgs(normalizedArgs);
  const codexArgs = explicitTask === 'ralph-cli-launch' && approvedHint?.task
    ? [...codexArgsBase, approvedHint.task]
    : codexArgsBase;
  const appendixPath = sessionFiles.instructionsPath;
  const previousAppendixEnv = process.env[RALPH_APPEND_ENV];
  process.env[RALPH_APPEND_ENV] = appendixPath;
  try {
    await launchWithHud(codexArgs);
  } finally {
    if (typeof previousAppendixEnv === 'string') process.env[RALPH_APPEND_ENV] = previousAppendixEnv;
    else delete process.env[RALPH_APPEND_ENV];
  }
}