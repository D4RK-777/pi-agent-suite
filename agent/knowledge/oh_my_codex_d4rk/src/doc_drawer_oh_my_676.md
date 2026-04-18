(join(tmpdir(), `${product}-${platform}-${arch}-`));
  const extractDir = join(tempRoot, 'extract');

  try {
    for (let index = 0; index < assets.length; index += 1) {
      const asset = assets[index]!;
      const archivePath = join(tempRoot, asset.archive);
      const cachedBinaryPath = resolveCachedNativeBinaryPath(
        product,
        version,
        platform,
        arch,
        env,
        inferNativeAssetLibc(asset),
      );
      try {
        await downloadFile(asset.download_url, archivePath);
        const archiveStat = await stat(archivePath);
        if (typeof asset.size === 'number' && asset.size > 0 && archiveStat.size !== asset.size) {
          throw new Error(`[native-assets] downloaded archive size mismatch for ${asset.archive}`);
        }