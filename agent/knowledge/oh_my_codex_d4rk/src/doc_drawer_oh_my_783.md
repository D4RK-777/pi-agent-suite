mmary.backedUp += 1;
  }

  if (!options.dryRun) {
    await writeFile(configPath, finalConfig);
  }

  if (
    options.verbose &&
    modelOverride &&
    currentModel &&
    currentModel !== modelOverride
  ) {
    console.log(
      `  ${options.dryRun ? "would update" : "updated"} root model from ${currentModel} to ${modelOverride}`,
    );
  }

  summary.updated += 1;
  if (options.verbose) {
    console.log(
      `  ${options.dryRun ? "would update" : "updated"} config ${configPath}`,
    );
  }
  return { finalConfig, omxManagesTui };
}

function getClaudeCodeSettingsPath(homeDir = homedir()): string {
  return join(homeDir, ".claude", "settings.json");
}