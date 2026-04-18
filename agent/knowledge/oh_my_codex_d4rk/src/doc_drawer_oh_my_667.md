ightRank) return leftRank - rightRank;
    return left.archive.localeCompare(right.archive);
  });
}

export function isRepositoryCheckout(packageRoot = getPackageRoot()): boolean {
  return existsSync(join(packageRoot, '.git')) || existsSync(join(packageRoot, 'src'));
}

export async function loadNativeReleaseManifest(
  packageRoot = getPackageRoot(),
  version?: string,
  env: NodeJS.ProcessEnv = process.env,
): Promise<NativeReleaseManifest> {
  const url = await resolveNativeManifestUrl(packageRoot, version, env);
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`[native-assets] failed to fetch native release manifest (${response.status} ${response.statusText}) from ${url}`);
  }
  return await response.json() as NativeReleaseManifest;
}