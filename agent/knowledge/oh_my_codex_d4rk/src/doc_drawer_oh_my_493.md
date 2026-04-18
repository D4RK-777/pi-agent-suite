}

  return {
    ...(prompt ? { prompt } : {}),
    ...(promptFile ? { promptFile } : {}),
  };
}

export function resolveExploreHarnessCommand(
  packageRoot = getPackageRoot(),
  env: NodeJS.ProcessEnv = process.env,
): ExploreHarnessCommand {
  const override = env[EXPLORE_BIN_ENV]?.trim();
  if (override) {
    return { command: isAbsolute(override) ? override : join(packageRoot, override), args: [] };
  }

  const packaged = resolvePackagedExploreHarnessCommand(packageRoot);
  if (packaged) return packaged;

  const repoBuilt = repoBuiltExploreHarnessCommand(packageRoot);
  if (repoBuilt) return repoBuilt;