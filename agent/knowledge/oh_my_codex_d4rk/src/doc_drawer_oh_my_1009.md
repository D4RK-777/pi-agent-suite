}> {
  const configPath = tmuxHookConfigPath(cwd);
  let initResult: InitConfigResult | null = null;

  if (!existsSync(configPath)) {
    initResult = await initTmuxHookConfig({ silent: true, cwd });
    if (initResult.created) {
      console.log(`No tmux-hook config found. Created ${initResult.configPath}.`);
      if (initResult.detectedSession) {
        console.log(`Detected tmux session: ${initResult.detectedSession}`);
      }
      if (initResult.usedPlaceholderTarget) {
        console.log('Could not auto-detect a tmux target. Edit `.omx/tmux-hook.json` when ready.');
        if (commandName === 'validate') {
          console.log('Validation skipped until `target.value` is configured.');
        }
      }
    }
  }