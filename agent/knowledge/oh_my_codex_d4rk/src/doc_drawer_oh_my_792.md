er === 'number' && Number.isFinite(signalNumber)) {
    return 128 + signalNumber;
  }
  return 1;
}

export function sparkshellBinaryName(platform: NodeJS.Platform = process.platform): string {
  return platform === 'win32' ? 'omx-sparkshell.exe' : 'omx-sparkshell';
}

export function packagedSparkShellBinaryPath(
  packageRoot = getPackageRoot(),
  platform: NodeJS.Platform = process.platform,
  arch: string = osArch(),
  libc?: 'musl' | 'glibc',
): string {
  const platformKey = libc ? `${platform}-${arch}-${libc}` : `${platform}-${arch}`;
  return join(packageRoot, 'bin', 'native', platformKey, sparkshellBinaryName(platform));
}