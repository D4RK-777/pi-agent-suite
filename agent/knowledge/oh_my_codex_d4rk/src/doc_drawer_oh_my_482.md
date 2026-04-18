es((subcommand || '').toLowerCase());
  }
  return ['find', 'ls', 'rg', 'grep'].includes(command);
}

export function resolveExploreSparkShellRoute(prompt: string): ExploreSparkShellRoute | undefined {
  const explicitShellPrefix = EXPLICIT_SHELL_PREFIX_PATTERN.test(prompt.trim());
  const normalized = prompt.trim().replace(EXPLICIT_SHELL_PREFIX_PATTERN, '');
  const argv = tokenizeExploreShellCommand(normalized);
  if (!argv || argv.length === 0) return undefined;

  const command = argv[0]?.toLowerCase();
  if (!command) return undefined;

  if (command === 'git' && isReadOnlyGitArgs(argv)) {
    return {
      argv,
      reason: classifyLongOutputShellCommand(argv) ? 'long-output' : 'shell-native',
    };
  }