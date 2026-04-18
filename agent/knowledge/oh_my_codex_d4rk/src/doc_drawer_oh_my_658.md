tiveReleaseBaseUrl(packageRoot, version, env);
  return `${baseUrl}/native-release-manifest.json`;
}

export function resolveNativeCacheRoot(env: NodeJS.ProcessEnv = process.env): string {
  const override = env[NATIVE_CACHE_DIR_ENV]?.trim();
  if (override) return resolve(override);
  if (process.platform === 'win32') {
    return resolve(env.LOCALAPPDATA?.trim() || join(homedir(), 'AppData', 'Local'), 'oh-my-codex', 'native');
  }
  return resolve(env.XDG_CACHE_HOME?.trim() || join(homedir(), '.cache'), 'oh-my-codex', 'native');
}