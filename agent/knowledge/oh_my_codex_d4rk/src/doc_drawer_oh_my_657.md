?? await getPackageVersion(packageRoot);
  return `${repo}/releases/download/v${resolvedVersion}`;
}

export async function resolveNativeManifestUrl(
  packageRoot = getPackageRoot(),
  version?: string,
  env: NodeJS.ProcessEnv = process.env,
): Promise<string> {
  const override = env[NATIVE_MANIFEST_URL_ENV]?.trim();
  if (override) return override;
  const baseUrl = await resolveNativeReleaseBaseUrl(packageRoot, version, env);
  return `${baseUrl}/native-release-manifest.json`;
}