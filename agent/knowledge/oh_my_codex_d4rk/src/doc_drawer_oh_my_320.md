ageError('Missing prompt text.');
  }

  let agentPromptRole: string | undefined;
  let prompt = '';

  for (let i = 0; i < rest.length; i += 1) {
    const token = rest[i];
    if (token === ASK_AGENT_PROMPT_FLAG) {
      const role = rest[i + 1]?.trim();
      if (!role || role.startsWith('-')) {
        throw askUsageError('Missing role after --agent-prompt.');
      }
      agentPromptRole = role;
      i += 1;
      continue;
    }
    if (token.startsWith(`${ASK_AGENT_PROMPT_FLAG}=`)) {
      const role = token.slice(`${ASK_AGENT_PROMPT_FLAG}=`.length).trim();
      if (!role) {
        throw askUsageError('Missing role after --agent-prompt=');
      }
      agentPromptRole = role;
      continue;
    }
    if (token === '-p' || token === '--print' || token === '--prompt') {