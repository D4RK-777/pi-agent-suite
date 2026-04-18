ush(packagedSparkShellBinaryPath(packageRoot, platform, arch));
  return [...new Set(candidates)];
}

export function repoLocalSparkShellBinaryPath(
  packageRoot = getPackageRoot(),
  platform: NodeJS.Platform = process.platform,
): string {
  return join(packageRoot, 'target', 'release', sparkshellBinaryName(platform));
}

export function nestedRepoLocalSparkShellBinaryPath(
  packageRoot = getPackageRoot(),
  platform: NodeJS.Platform = process.platform,
): string {
  return join(packageRoot, 'native', 'omx-sparkshell', 'target', 'release', sparkshellBinaryName(platform));
}