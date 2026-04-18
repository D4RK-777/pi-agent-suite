console.log(
      `  Native agent refresh complete (${scopeDirs.nativeAgentsDir}).\n`,
    );
  }

  // Step 5: Update config.toml
  console.log("[5/8] Updating config.toml...");
  const registryCandidates = getUnifiedMcpRegistryCandidates();
  const defaultRegistryCandidates = registryCandidates.slice(0, 1);
  const sharedMcpRegistry = await loadUnifiedMcpRegistry({
    candidates: options.mcpRegistryCandidates ?? defaultRegistryCandidates,
  });
  if (
    !options.mcpRegistryCandidates &&
    !sharedMcpRegistry.sourcePath &&
    registryCandidates.length > 1 &&
    existsSync(registryCandidates[1]) &&
    !existsSync(registryCandidates[0])
  ) {
    console.log(