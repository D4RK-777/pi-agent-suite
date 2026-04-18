';
  if (hint.includes('linux-gnu') || hint.includes('glibc')) return 'glibc';
  return undefined;
}

export function resolveCachedNativeBinaryCandidatePaths(
  product: NativeProduct,
  version: string,
  platform: NodeJS.Platform = process.platform,
  arch: string = process.arch,
  env: NodeJS.ProcessEnv = process.env,
  options: NativeBinaryCandidateOptions = {},
): string[] {
  const candidates: string[] = [];
  if (platform === 'linux') {
    for (const libc of options.linuxLibcPreference ?? resolveLinuxNativeLibcPreference({ env })) {
      candidates.push(resolveCachedNativeBinaryPath(product, version, platform, arch, env, libc));
    }
  }
  candidates.push(resolveCachedNativeBinaryPath(product, version, platform, arch, env));
  return [...new Set(candidates)];
}