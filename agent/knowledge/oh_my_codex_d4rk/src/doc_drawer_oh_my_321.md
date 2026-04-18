role;
      continue;
    }
    if (token === '-p' || token === '--print' || token === '--prompt') {
      prompt = rest.slice(i + 1).join(' ').trim();
      break;
    }
    if (token.startsWith('-p=') || token.startsWith('--print=') || token.startsWith('--prompt=')) {
      const inlinePrompt = token.split('=').slice(1).join('=').trim();
      const remainder = rest.slice(i + 1).join(' ').trim();
      prompt = [inlinePrompt, remainder].filter(Boolean).join(' ').trim();
      break;
    }
    prompt = [prompt, token].filter(Boolean).join(' ').trim();
  }

  if (!prompt) {
    throw askUsageError('Missing prompt text.');
  }

  return {
    provider: provider as AskProvider,
    prompt,
    ...(agentPromptRole ? { agentPromptRole } : {}),
  };
}