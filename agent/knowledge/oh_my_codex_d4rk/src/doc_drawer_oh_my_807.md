as NodeJS.ErrnoException;
    const kind = classifySpawnError(errno);
    if (kind === 'missing') {
      throw new Error(`[sparkshell] raw fallback failed: executable not found (${invocation.argv[0]})`);
    }
    if (kind === 'blocked') {
      throw new Error(`[sparkshell] raw fallback failed: executable is blocked (${errno.code || 'blocked'})`);
    }
    throw new Error(`[sparkshell] raw fallback failed: ${errno.message}`);
  }
  if (result.status !== 0) {
    process.exitCode = typeof result.status === 'number'
      ? result.status
      : resolveSignalExitCode(result.signal);
  }
}

export async function sparkshellCommand(args: string[]): Promise<void> {
  if (args[0] === '--help' || args[0] === '-h') {
    console.log(SPARKSHELL_USAGE);
    return;
  }