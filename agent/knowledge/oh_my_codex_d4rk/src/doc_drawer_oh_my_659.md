return resolve(env.XDG_CACHE_HOME?.trim() || join(homedir(), '.cache'), 'oh-my-codex', 'native');
}

export function resolveCachedNativeBinaryPath(
  product: NativeProduct,
  version: string,
  platform: NodeJS.Platform = process.platform,
  arch: string = process.arch,
  env: NodeJS.ProcessEnv = process.env,
  libc?: NativeLibc,
): string {
  const binary = platform === 'win32' ? `${product}.exe` : product;
  const platformKey = libc ? `${platform}-${arch}-${libc}` : `${platform}-${arch}`;
  return join(resolveNativeCacheRoot(env), version, platformKey, product, binary);
}

const MUSL_LOADER_DIRS = ['/lib', '/lib64', '/usr/lib', '/usr/local/lib'];
const MUSL_LOADER_PATTERN = /^ld-musl-.*\.so(?:\.\d+)*$/i;