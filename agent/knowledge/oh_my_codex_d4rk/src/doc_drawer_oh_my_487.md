orm !== platform) return undefined;
    if (expectedArch && expectedArch !== arch) return undefined;
    const binaryName = metadata.binaryName?.trim() || packagedExploreHarnessBinaryName(platform);
    const binaryPath = join(packageRoot, 'bin', binaryName);
    if (!existsSync(binaryPath)) return undefined;
    return { command: binaryPath, args: [] };
  } catch {
    return undefined;
  }
}

export function repoBuiltExploreHarnessCommand(
  packageRoot = getPackageRoot(),
  platform: NodeJS.Platform = process.platform,
): ExploreHarnessCommand | undefined {
  const binaryName = packagedExploreHarnessBinaryName(platform);
  for (const mode of ['release', 'debug'] as const) {
    const binaryPath = join(packageRoot, 'target', mode, binaryName);
    if (existsSync(binaryPath)) {