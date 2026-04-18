(`[ask] --agent-prompt role "${normalizedRole}" not found in ${promptsDir}.${availableSuffix}`);
  }

  const content = (await readFile(promptPath, 'utf-8')).trim();
  if (!content) {
    throw new Error(`[ask] --agent-prompt role "${normalizedRole}" is empty: ${promptPath}`);
  }

  return content;
}

export function parseAskArgs(args: readonly string[]): ParsedAskArgs {
  const [providerRaw, ...rest] = args;
  const provider = (providerRaw || '').toLowerCase();

  if (!provider || !ASK_PROVIDER_SET.has(provider)) {
    throw askUsageError(`Invalid provider "${providerRaw || ''}". Expected one of: ${ASK_PROVIDERS.join(', ')}.`);
  }

  if (rest.length === 0) {
    throw askUsageError('Missing prompt text.');
  }

  let agentPromptRole: string | undefined;
  let prompt = '';