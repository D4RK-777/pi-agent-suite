visorScriptPath)) {
    throw new Error(`[ask] advisor script not found: ${advisorScriptPath}`);
  }

  let finalPrompt = parsed.prompt;
  if (parsed.agentPromptRole) {
    const agentPromptContent = await resolveAgentPromptContent(parsed.agentPromptRole, promptsDir);
    finalPrompt = `${agentPromptContent}\n\n${parsed.prompt}`;
  }

  const child = spawnSync(
    process.execPath,
    [advisorScriptPath, parsed.provider, finalPrompt],
    {
      cwd: process.cwd(),
      env: {
        ...process.env,
        [ASK_ORIGINAL_TASK_ENV]: parsed.prompt,
      },
      stdio: ['ignore', 'pipe', 'pipe'],
    },
  );