UP_MODEL);
      if (shouldUpgrade) {
        modelOverride = DEFAULT_SETUP_MODEL;
      }
    }
  }

  const finalConfig = buildMergedConfig(existing, pkgRoot, {
    includeTui: omxManagesTui,
    modelOverride,
    sharedMcpServers: sharedMcpRegistry.servers,
    sharedMcpRegistrySource: sharedMcpRegistry.sourcePath,
    verbose: options.verbose,
  });
  const changed = existing !== finalConfig;

  if (!changed) {
    summary.unchanged += 1;
    return { finalConfig, omxManagesTui };
  }

  if (
    await ensureBackup(
      configPath,
      existsSync(configPath),
      backupContext,
      options,
    )
  ) {
    summary.backedUp += 1;
  }

  if (!options.dryRun) {
    await writeFile(configPath, finalConfig);
  }