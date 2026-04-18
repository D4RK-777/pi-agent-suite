esult.stdout);
  if (result.stderr && result.stderr.length > 0) process.stderr.write(result.stderr);

  if (result.error) {
    const errno = result.error as NodeJS.ErrnoException;
    if (harness.command === 'cargo' && errno.code === 'ENOENT') {
      throw new Error('[explore] cargo was not found. Install a Rust toolchain, use a compatible packaged omx-explore prebuilt, or set OMX_EXPLORE_BIN to a prebuilt harness binary.');
    }
    throw new Error(`[explore] failed to launch harness: ${result.error.message}`);
  }

  if (result.status !== 0) {
    process.exitCode = result.status ?? 1;
  }
}