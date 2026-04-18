version, platform, arch, env)) {
    if (existsSync(cachedBinaryPath)) return cachedBinaryPath;
  }

  let manifest: NativeReleaseManifest;
  try {
    manifest = await loadNativeReleaseManifest(packageRoot, version, env);
  } catch (error) {
    if (isUnavailableManifestError(error)) return undefined;
    throw error;
  }
  const assets = resolveNativeReleaseAssetCandidates(manifest, product, version, platform, arch, {
    linuxLibcPreference: platform === 'linux' ? resolveLinuxNativeLibcPreference({ env }) : undefined,
  });
  if (assets.length === 0) return undefined;

  const tempRoot = await mkdtemp(join(tmpdir(), `${product}-${platform}-${arch}-`));
  const extractDir = join(tempRoot, 'extract');