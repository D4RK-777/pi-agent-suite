{
    command: 'cargo',
    args: ['run', '--quiet', '--manifest-path', manifestPath, '--'],
  };
}

export async function resolveExploreHarnessCommandWithHydration(
  packageRoot = getPackageRoot(),
  env: NodeJS.ProcessEnv = process.env,
): Promise<ExploreHarnessCommand> {
  const override = env[EXPLORE_BIN_ENV]?.trim();
  if (override) {
    return { command: isAbsolute(override) ? override : join(packageRoot, override), args: [] };
  }

  const version = await getPackageVersion(packageRoot);
  for (const cached of resolveCachedNativeBinaryCandidatePaths('omx-explore-harness', version, process.platform, process.arch, env)) {
    if (existsSync(cached)) {
      return { command: cached, args: [] };
    }
  }