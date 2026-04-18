' -Force`]
        : ['-oq', archivePath, '-d', destinationDir],
      { encoding: 'utf-8' },
    );
    if (result.status !== 0 || result.error) {
      throw new Error(`[native-assets] failed to extract zip archive ${archivePath}: ${(result.stderr || result.error?.message || '').trim()}`);
    }
    return;
  }

  const { result } = spawnPlatformCommandSync('tar', ['-xf', archivePath, '-C', destinationDir], { encoding: 'utf-8' });
  if (result.status !== 0 || result.error) {
    throw new Error(`[native-assets] failed to extract archive ${archivePath}: ${(result.stderr || result.error?.message || '').trim()}`);
  }
}