t(),
    env = process.env,
    platform = process.platform,
    arch = process.arch,
  } = options;

  if (env[NATIVE_AUTO_FETCH_ENV]?.trim() === '0') return undefined;
  if (!['linux', 'darwin', 'win32'].includes(platform)) return undefined;
  if (!['x64', 'arm64'].includes(arch)) return undefined;

  const version = await getPackageVersion(packageRoot);
  for (const cachedBinaryPath of resolveCachedNativeBinaryCandidatePaths(product, version, platform, arch, env)) {
    if (existsSync(cachedBinaryPath)) return cachedBinaryPath;
  }