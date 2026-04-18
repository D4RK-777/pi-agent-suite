ring[]): ParsedExploreArgs {
  let prompt: string | undefined;
  let promptFile: string | undefined;

  for (let i = 0; i < args.length; i += 1) {
    const token = args[i];
    if (token === PROMPT_FLAG) {
      const remaining = args.slice(i + 1);
      if (remaining.length === 0 || remaining[0].startsWith('-')) {
        throw exploreUsageError('Missing text after --prompt.');
      }
      if (hasPromptSource(remaining, PROMPT_FILE_FLAG)) {
        throw exploreUsageError('Choose exactly one of --prompt or --prompt-file.');
      }
      prompt = appendPromptValue(prompt, remaining.join(' '), 'Missing text after --prompt.');
      break;
    }
    if (token.startsWith(`${PROMPT_FLAG}=`)) {
      const remaining = args.slice(i + 1);