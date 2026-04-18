eak;
    }
    if (token.startsWith(`${PROMPT_FLAG}=`)) {
      const remaining = args.slice(i + 1);
      if (hasPromptSource(remaining, PROMPT_FILE_FLAG)) {
        throw exploreUsageError('Choose exactly one of --prompt or --prompt-file.');
      }
      prompt = appendPromptValue(prompt, token.slice(`${PROMPT_FLAG}=`.length), 'Missing text after --prompt=.');
      continue;
    }
    if (token === PROMPT_FILE_FLAG) {
      const value = args[i + 1];
      if (!value || value.startsWith('-')) throw exploreUsageError('Missing path after --prompt-file.');
      promptFile = appendPromptFileValue(promptFile, value, 'Missing path after --prompt-file.');
      i += 1;
      continue;
    }
    if (token.startsWith(`${PROMPT_FILE_FLAG}=`)) {