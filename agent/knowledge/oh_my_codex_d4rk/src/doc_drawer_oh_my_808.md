if (args[0] === '--help' || args[0] === '-h') {
    console.log(SPARKSHELL_USAGE);
    return;
  }

  if (args.length === 0) {
    throw new Error(`Missing command to run.\n${SPARKSHELL_USAGE}`);
  }

  const hasExplicitOverride = typeof process.env[OMX_SPARKSHELL_BIN_ENV] === 'string'
    && process.env[OMX_SPARKSHELL_BIN_ENV]!.trim().length > 0;
  let binaryPath: string;
  try {
    binaryPath = await resolveSparkShellBinaryPathWithHydration();
  } catch (error) {
    if (!hasExplicitOverride) {
      runSparkShellFallback(args);
      return;
    }
    throw error;
  }
  const result = runSparkShellBinary(binaryPath, args);