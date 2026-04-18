alse;
  const configPath = tmuxHookConfigPath(cwd);
  await mkdir(omxDir(cwd), { recursive: true });

  if (existsSync(configPath)) {
    if (!silent) {
      console.log(`tmux-hook config already exists: ${configPath}`);
    }
    return { configPath, created: false, usedPlaceholderTarget: false };
  }

  const detected = detectInitialTarget();
  const initial = {
    ...DEFAULT_CONFIG,
    target: detected?.target ?? { type: 'pane' as const, value: 'replace-with-tmux-pane-id' },
  };
  await writeFile(configPath, JSON.stringify(initial, null, 2) + '\n');

  const result: InitConfigResult = {
    configPath,
    created: true,
    usedPlaceholderTarget: !detected,
    detectedSession: detected?.sessionName,
  };