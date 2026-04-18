= process.cwd();
  const statePath = tmuxHookStatePath(cwd);
  const logPath = tmuxHookLogPath(cwd);

  console.log('tmux-hook status');
  console.log('----------------');
  const { config, initResult } = await loadConfigForCommand('status', cwd);
  const configPath = tmuxHookConfigPath(cwd);
  console.log(`Config: ${configPath}`);
  console.log(`Enabled: ${config.enabled ? 'yes' : 'no'}`);
  console.log(`Target: ${config.target.type}:${config.target.value}`);
  if (initResult?.usedPlaceholderTarget) {
    console.log('Target Status: placeholder (set `target.value` to enable injection)');
  }
  console.log(`Allowed Modes: ${config.allowed_modes.join(', ')}`);
  console.log(`Cooldown: ${config.cooldown_ms}ms`);
  console.log(`Max Injections/Pane: ${config.max_injections_per_session}`);