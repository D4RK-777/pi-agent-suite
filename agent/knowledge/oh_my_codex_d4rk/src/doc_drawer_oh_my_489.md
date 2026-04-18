(current !== undefined) throw exploreUsageError('Duplicate --prompt provided.');
  return trimmed;
}

function appendPromptFileValue(current: string | undefined, value: string, reason: string): string {
  const trimmed = value.trim();
  if (!trimmed) throw exploreUsageError(reason);
  if (current !== undefined) throw exploreUsageError('Duplicate --prompt-file provided.');
  return trimmed;
}

function hasPromptSource(tokens: readonly string[], flag: string): boolean {
  return tokens.some((token) => token === flag || token.startsWith(`${flag}=`));
}

export function parseExploreArgs(args: readonly string[]): ParsedExploreArgs {
  let prompt: string | undefined;
  let promptFile: string | undefined;