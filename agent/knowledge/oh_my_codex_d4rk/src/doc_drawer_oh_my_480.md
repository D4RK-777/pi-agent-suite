trimmed || SHELL_ROUTE_DISALLOWED_PATTERN.test(trimmed) || trimmed.includes('\\')) return undefined;

  const tokens = trimmed.match(/"[^"]*"|'[^']*'|\S+/g);
  if (!tokens) return undefined;
  return tokens.map((token) => {
    if ((token.startsWith('\"') && token.endsWith('\"')) || (token.startsWith("'") && token.endsWith("'"))) {
      return token.slice(1, -1);
    }
    return token;
  });
}

function isReadOnlyGitArgs(args: readonly string[]): boolean {
  const subcommand = args[1]?.toLowerCase();
  if (!subcommand || !READ_ONLY_GIT_SUBCOMMANDS.has(subcommand)) return false;
  if (subcommand === 'diff') {
    return args.some((arg) => /^--(?:stat|name-only|name-status|numstat|shortstat)$/.test(arg));
  }
  if (subcommand === 'show') {