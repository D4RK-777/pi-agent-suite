Error(`[ask] prompts directory not found: ${promptsDir}. Run "omx setup" to install prompts.`);
  }

  const promptPath = join(promptsDir, `${normalizedRole}.md`);
  if (!existsSync(promptPath)) {
    const files = await readdir(promptsDir).catch(() => [] as string[]);
    const availableRoles = files
      .filter((file) => file.endsWith('.md'))
      .map((file) => file.slice(0, -3))
      .sort();
    const availableSuffix = availableRoles.length > 0
      ? ` Available roles: ${availableRoles.join(', ')}.`
      : '';
    throw new Error(`[ask] --agent-prompt role "${normalizedRole}" not found in ${promptsDir}.${availableSuffix}`);
  }