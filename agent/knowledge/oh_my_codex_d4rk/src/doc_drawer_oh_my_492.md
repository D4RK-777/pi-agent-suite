mpt-file.');
      i += 1;
      continue;
    }
    if (token.startsWith(`${PROMPT_FILE_FLAG}=`)) {
      promptFile = appendPromptFileValue(promptFile, token.slice(`${PROMPT_FILE_FLAG}=`.length), 'Missing path after --prompt-file=.');
      continue;
    }
    throw exploreUsageError(`Unknown argument: ${token}`);
  }

  if (prompt && promptFile) {
    throw exploreUsageError('Choose exactly one of --prompt or --prompt-file.');
  }
  if (!prompt && !promptFile) {
    throw exploreUsageError('Missing prompt. Provide --prompt or --prompt-file.');
  }

  return {
    ...(prompt ? { prompt } : {}),
    ...(promptFile ? { promptFile } : {}),
  };
}