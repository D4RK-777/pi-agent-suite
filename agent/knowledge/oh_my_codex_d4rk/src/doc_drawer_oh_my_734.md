N.stringify(payload, null, 2) + "\n");
  if (options.verbose) console.log(`  Wrote ${scopePath}`);
}

export async function setup(options: SetupOptions = {}): Promise<void> {
  const {
    force = false,
    dryRun = false,
    scope: requestedScope,
    verbose = false,
    modelUpgradePrompt,
  } = options;
  const pkgRoot = getPackageRoot();
  const projectRoot = process.cwd();
  const resolvedScope = await resolveSetupScope(projectRoot, requestedScope);
  const scopeDirs = resolveScopeDirectories(resolvedScope.scope, projectRoot);
  const scopeSourceMessage =
    resolvedScope.source === "persisted" ? " (from .omx/setup-scope.json)" : "";
  const backupContext = getBackupContext(resolvedScope.scope, projectRoot);