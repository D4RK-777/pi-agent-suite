form): string {
  return platform === 'win32' ? 'omx-explore-harness.exe' : 'omx-explore-harness';
}

export function resolvePackagedExploreHarnessCommand(
  packageRoot = getPackageRoot(),
  platform: NodeJS.Platform = process.platform,
  arch = process.arch,
): ExploreHarnessCommand | undefined {
  const metadataPath = join(packageRoot, 'bin', 'omx-explore-harness.meta.json');
  if (!existsSync(metadataPath)) return undefined;
  try {
    const metadata = JSON.parse(readFileSync(metadataPath, 'utf-8')) as ExploreHarnessMetadata;
    const expectedPlatform = metadata.platform?.trim();
    const expectedArch = metadata.arch?.trim();
    if (expectedPlatform && expectedPlatform !== platform) return undefined;
    if (expectedArch && expectedArch !== arch) return undefined;