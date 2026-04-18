.startsWith('http://github.com/')) return trimmed.replace(/^http:/, 'https:');
  return undefined;
}

export async function resolveNativeReleaseBaseUrl(
  packageRoot = getPackageRoot(),
  version?: string,
  env: NodeJS.ProcessEnv = process.env,
): Promise<string> {
  const override = env[NATIVE_RELEASE_BASE_URL_ENV]?.trim();
  if (override) return override.replace(/\/$/, '');
  const pkg = await readPackageJson(packageRoot);
  const repo = repositoryHttpBase(pkg.repository);
  if (!repo) throw new Error('[native-assets] unable to resolve GitHub repository URL for native release downloads');
  const resolvedVersion = version ?? await getPackageVersion(packageRoot);
  return `${repo}/releases/download/v${resolvedVersion}`;
}