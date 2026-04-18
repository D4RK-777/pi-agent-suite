cation hook...");
  await setupNotifyHook(pkgRoot, { dryRun, verbose });
  console.log("  Done.\n");

  // Step 8: Configure HUD
  console.log("[8/8] Configuring HUD...");
  const hudConfigPath = join(projectRoot, ".omx", "hud-config.json");
  if (force || !existsSync(hudConfigPath)) {
    if (!dryRun) {
      const defaultHudConfig = { preset: "focused" };
      await writeFile(hudConfigPath, JSON.stringify(defaultHudConfig, null, 2));
    }
    if (verbose) console.log("  Wrote .omx/hud-config.json");
    console.log("  HUD config created (preset: focused).");
  } else {
    console.log("  HUD config already exists (use --force to overwrite).");
  }
  if (managedConfig.omxManagesTui) {
    console.log("  StatusLine configured in config.toml via [tui] section.");
  } else {