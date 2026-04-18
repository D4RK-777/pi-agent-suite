k so OMX can fetch the release asset, or set ${OMX_SPARKSHELL_BIN_ENV} to override the path.`
  );
}

export function runSparkShellBinary(
  binaryPath: string,
  args: readonly string[],
  options: RunSparkShellBinaryOptions = {},
): SpawnSyncReturns<string> {
  const {
    cwd = process.cwd(),
    env = process.env,
    spawnImpl = spawnSync,
  } = options;

  const configEnvOverrides = readConfiguredEnvOverrides(env.CODEX_HOME);
  const spawnOptions: SpawnSyncOptionsWithStringEncoding = {
    cwd,
    env: { ...configEnvOverrides, ...env },
    stdio: ['ignore', 'pipe', 'pipe'],
    encoding: 'utf-8',
  };

  return spawnImpl(binaryPath, [...args], spawnOptions);
}