s);
      return;
    }
    throw error;
  }
  const result = runSparkShellBinary(binaryPath, args);

  if (result.error) {
    const errno = result.error as NodeJS.ErrnoException;
    const kind = classifySpawnError(errno);
    if (!hasExplicitOverride && (kind === 'missing' || kind === 'blocked')) {
      runSparkShellFallback(args);
      return;
    }
    if (kind === 'missing') {
      throw new Error(`[sparkshell] failed to launch native binary: executable not found (${binaryPath})`);
    }
    if (kind === 'blocked') {
      throw new Error(`[sparkshell] failed to launch native binary: executable is blocked (${errno.code || 'blocked'})`);
    }
    throw new Error(`[sparkshell] failed to launch native binary: ${errno.message}`);
  }