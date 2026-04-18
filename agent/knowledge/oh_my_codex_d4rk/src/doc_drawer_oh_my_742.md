existsSync(registryCandidates[1]) &&
    !existsSync(registryCandidates[0])
  ) {
    console.log(
      `  warning: legacy shared MCP registry detected at ${registryCandidates[1]} but ignored by default; move it to ${registryCandidates[0]} if you still want setup to sync those servers`,
    );
  }
  if (verbose && sharedMcpRegistry.sourcePath) {
    console.log(
      `  shared MCP registry: ${sharedMcpRegistry.sourcePath} (${sharedMcpRegistry.servers.length} servers)`,
    );
  }
  for (const warning of sharedMcpRegistry.warnings) {
    console.log(`  warning: ${warning}`);
  }
  const managedConfig = await updateManagedConfig(
    scopeDirs.codexConfigFile,
    pkgRoot,
    sharedMcpRegistry,
    summary.config,
    backupContext,