e', 'pipe'],
    encoding: 'utf-8',
  };

  return spawnImpl(binaryPath, [...args], spawnOptions);
}

function writeSparkShellResultOutput(result: SpawnSyncReturns<string>): void {
  if (typeof result.stdout === 'string' && result.stdout.length > 0) process.stdout.write(result.stdout);
  if (typeof result.stderr === 'string' && result.stderr.length > 0) process.stderr.write(result.stderr);
}

const SPARKSHELL_GLIBC_INCOMPATIBLE_PATTERN = /GLIBC(?:XX)?_[0-9.]+['` ]+not found/i;

export function isSparkShellNativeCompatibilityFailure(result: SpawnSyncReturns<string>): boolean {
  if ((result.status ?? 0) === 0) return false;
  return SPARKSHELL_GLIBC_INCOMPATIBLE_PATTERN.test(result.stderr || '');
}