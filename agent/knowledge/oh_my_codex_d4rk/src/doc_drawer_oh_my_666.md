et.platform === platform
    && asset.arch === arch);
  if (platform !== 'linux') return candidates;

  const preference = options.linuxLibcPreference ?? resolveLinuxNativeLibcPreference();
  const preferenceIndex = new Map(preference.map((libc, index) => [libc, index]));
  return [...candidates].sort((left, right) => {
    const leftLibc = inferNativeAssetLibc(left);
    const rightLibc = inferNativeAssetLibc(right);
    const leftRank = leftLibc ? (preferenceIndex.get(leftLibc) ?? preference.length + 1) : preference.length;
    const rightRank = rightLibc ? (preferenceIndex.get(rightLibc) ?? preference.length + 1) : preference.length;
    if (leftRank !== rightRank) return leftRank - rightRank;
    return left.archive.localeCompare(right.archive);
  });
}