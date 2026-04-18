const binaryPath = join(packageRoot, 'target', mode, binaryName);
    if (existsSync(binaryPath)) {
      return { command: binaryPath, args: [] };
    }
  }
  return undefined;
}

function exploreUsageError(reason: string): Error {
  return new Error(`${reason}\n${EXPLORE_USAGE}`);
}

function appendPromptValue(current: string | undefined, value: string, reason: string): string {
  const trimmed = value.trim();
  if (!trimmed) throw exploreUsageError(reason);
  if (current !== undefined) throw exploreUsageError('Duplicate --prompt provided.');
  return trimmed;
}