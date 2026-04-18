oin(packageRoot, 'native', 'omx-sparkshell', 'target', 'release', sparkshellBinaryName(platform));
}

export function resolveSparkShellBinaryPath(options: ResolveSparkShellBinaryPathOptions = {}): string {
  const {
    cwd = process.cwd(),
    env = process.env,
    packageRoot = getPackageRoot(),
    platform = process.platform,
    arch = osArch(),
    linuxLibcPreference,
    exists = existsSync,
  } = options;

  const override = env[OMX_SPARKSHELL_BIN_ENV]?.trim();
  if (override) {
    return isAbsolute(override) ? override : resolve(cwd, override);
  }

  for (const packaged of packagedSparkShellBinaryCandidatePaths(packageRoot, platform, arch, env, linuxLibcPreference)) {
    if (exists(packaged)) return packaged;
  }