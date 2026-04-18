{arch}`;
  return join(packageRoot, 'bin', 'native', platformKey, sparkshellBinaryName(platform));
}

export function packagedSparkShellBinaryCandidatePaths(
  packageRoot = getPackageRoot(),
  platform: NodeJS.Platform = process.platform,
  arch: string = osArch(),
  env: NodeJS.ProcessEnv = process.env,
  linuxLibcPreference?: readonly ('musl' | 'glibc')[],
): string[] {
  const candidates: string[] = [];
  if (platform === 'linux') {
    for (const libc of linuxLibcPreference ?? resolveLinuxNativeLibcPreference({ env })) {
      candidates.push(packagedSparkShellBinaryPath(packageRoot, platform, arch, libc));
    }
  }
  candidates.push(packagedSparkShellBinaryPath(packageRoot, platform, arch));
  return [...new Set(candidates)];
}