us: 'warn',
      message: `OMX_EXPLORE_BIN is set but path was not found (${override})`,
    };
  }

  const packaged = resolvePackagedExploreHarnessCommand(packageRoot);
  if (packaged) {
    return {
      name: 'Explore Harness',
      status: 'pass',
      message: `ready (packaged native binary: ${packaged.command})`,
    };
  }

  const { result } = spawnPlatformCommandSync('cargo', ['--version'], {
    encoding: 'utf-8',
    stdio: ['pipe', 'pipe', 'pipe'],
  });
  if (result.error) {
    const kind = classifySpawnError(result.error as NodeJS.ErrnoException);
    if (kind === 'missing') {
      return {
        name: 'Explore Harness',
        status: 'warn',