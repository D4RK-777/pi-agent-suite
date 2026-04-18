_GIT_SUBCOMMANDS = new Set([
  'log',
  'diff',
  'status',
  'show',
  'branch',
  'rev-parse',
]);

const SHELL_ROUTE_DISALLOWED_PATTERN = /[|&;><`$()]/;
const EXPLICIT_SHELL_PREFIX_PATTERN = /^run\s+/i;

export interface ExploreSparkShellRoute {
  argv: string[];
  reason: 'shell-native' | 'long-output';
}

function tokenizeExploreShellCommand(commandText: string): string[] | undefined {
  const trimmed = commandText.trim();
  if (!trimmed || SHELL_ROUTE_DISALLOWED_PATTERN.test(trimmed) || trimmed.includes('\\')) return undefined;