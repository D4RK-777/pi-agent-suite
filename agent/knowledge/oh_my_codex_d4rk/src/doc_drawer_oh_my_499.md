!trimmed) throw exploreUsageError(`Prompt file is empty: ${parsed.promptFile}`);
  return trimmed;
}

export async function exploreCommand(args: string[]): Promise<void> {
  const parsed = parseExploreArgs(args);
  const prompt = await loadExplorePrompt(parsed);
  const sparkShellRoute = resolveExploreSparkShellRoute(prompt);
  if (sparkShellRoute) {
    try {
      await runExploreViaSparkShell(sparkShellRoute, process.env);
      return;
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      process.stderr.write(`[omx explore] sparkshell backend unavailable (${message}). Falling back to the explore harness.\n`);
    }
  }