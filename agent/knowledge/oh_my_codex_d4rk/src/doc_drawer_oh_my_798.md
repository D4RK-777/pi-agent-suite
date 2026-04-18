?.trim();
  if (override) {
    return isAbsolute(override) ? override : resolve(cwd, override);
  }

  const version = await getPackageVersion(packageRoot);
  for (const cached of resolveCachedNativeBinaryCandidatePaths('omx-sparkshell', version, platform, arch, env, {
    linuxLibcPreference: platform === 'linux'
      ? (linuxLibcPreference ?? resolveLinuxNativeLibcPreference({ env }))
      : undefined,
  })) {
    if (exists(cached)) return cached;
  }

  for (const packaged of packagedSparkShellBinaryCandidatePaths(packageRoot, platform, arch, env, linuxLibcPreference)) {
    if (exists(packaged)) return packaged;
  }

  const repoLocal = repoLocalSparkShellBinaryPath(packageRoot, platform);
  if (exists(repoLocal)) return repoLocal;