{
    dryRun = false,
    keepConfig = false,
    verbose = false,
    purge = false,
  } = options;

  const projectRoot = process.cwd();
  const pkgRoot = getPackageRoot();

  // Resolve scope (explicit --scope overrides persisted scope)
  const scope = options.scope ?? readPersistedSetupScope(projectRoot) ?? "user";
  const scopeDirs = resolveScopeDirectories(scope, projectRoot);

  console.log("oh-my-codex uninstall");
  console.log("=====================\n");
  if (dryRun) {
    console.log("[dry-run mode] No files will be modified.\n");
  }
  console.log(`Resolved scope: ${scope}\n`);