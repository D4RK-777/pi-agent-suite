beInstalledCodexVersion();
  const omxManagesTui = shouldOmxManageTuiFromCodexVersion(codexVersion);

  if (currentModel === LEGACY_SETUP_MODEL) {
    const shouldPrompt =
      typeof options.modelUpgradePrompt === "function" ||
      (process.stdin.isTTY && process.stdout.isTTY);
    if (shouldPrompt) {
      const shouldUpgrade = options.modelUpgradePrompt
        ? await options.modelUpgradePrompt(currentModel, DEFAULT_SETUP_MODEL)
        : await promptForModelUpgrade(currentModel, DEFAULT_SETUP_MODEL);
      if (shouldUpgrade) {
        modelOverride = DEFAULT_SETUP_MODEL;
      }
    }
  }