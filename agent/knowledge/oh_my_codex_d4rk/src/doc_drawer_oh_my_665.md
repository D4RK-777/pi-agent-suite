CachedNativeBinaryPath(product, version, platform, arch, env));
  return [...new Set(candidates)];
}

export function resolveNativeReleaseAssetCandidates(
  manifest: NativeReleaseManifest,
  product: NativeProduct,
  version: string,
  platform: NodeJS.Platform,
  arch: string,
  options: NativeBinaryCandidateOptions = {},
): NativeReleaseAsset[] {
  const candidates = manifest.assets.filter((asset) => asset.product === product
    && asset.version === version
    && asset.platform === platform
    && asset.arch === arch);
  if (platform !== 'linux') return candidates;