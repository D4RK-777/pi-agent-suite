nged-files.txt', noDeslop: options.noDeslop, approvedHint: options.approvedHint ?? null })}\n`,
  );
  return { instructionsPath, changedFilesPath: '.omx/ralph/changed-files.txt' };
}

export async function ralphCommand(args: string[]): Promise<void> {
  const normalizedArgs = normalizeRalphCliArgs(args);
  const cwd = process.cwd();
  if (normalizedArgs[0] === '--help' || normalizedArgs[0] === '-h') {
    console.log(RALPH_HELP);
    return;
  }
  const artifacts = await ensureCanonicalRalphArtifacts(cwd);
  const approvedHint = readApprovedExecutionLaunchHint(cwd, 'ralph');
  const explicitTask = extractRalphTaskDescription(normalizedArgs);
  const task = explicitTask === 'ralph-cli-launch' ? approvedHint?.task ?? explicitTask : explicitTask;