eePath, { runTag });
  await runAutoresearchLoop(codexArgs, runtime, worktreeContract.missionDir);
}

export async function autoresearchCommand(args: string[]): Promise<void> {
  const parsed = parseAutoresearchArgs(args);
  if (parsed.missionDir === '--help') {
    console.log(AUTORESEARCH_HELP);
    return;
  }

  if (parsed.guided) {
    const repoRoot = resolveRepoRoot(process.cwd());
    let result;
    if (parsed.initArgs && parsed.initArgs.length > 0) {
      const initOpts = parseInitArgs(parsed.initArgs);
      if (!initOpts.topic || !initOpts.evaluatorCommand || !initOpts.slug) {
        throw new Error(
          'init requires --topic, --evaluator, and --slug flags.\n'
          + 'Optional: --keep-policy (default: score_improvement)\n\n'
          + `${AUTORESEARCH_HELP}`,