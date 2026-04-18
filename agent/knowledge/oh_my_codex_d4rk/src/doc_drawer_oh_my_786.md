options,
    `Claude Code MCP settings ${settingsPath} (+${syncPlan.added.join(", ")})`,
  );
}

async function setupNotifyHook(
  pkgRoot: string,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
): Promise<void> {
  const hookScript = join(pkgRoot, "dist", "scripts", "notify-hook.js");
  if (!existsSync(hookScript)) {
    if (options.verbose)
      console.log("  Notify hook script not found, skipping.");
    return;
  }
  // The notify hook is configured in config.toml via mergeConfig
  if (options.verbose) console.log(`  Notify hook: ${hookScript}`);
}