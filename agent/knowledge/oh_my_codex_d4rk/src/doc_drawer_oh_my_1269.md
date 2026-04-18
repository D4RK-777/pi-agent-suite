chunk : Buffer.from(chunk).toString('utf-8'));
    return true;
  }) as typeof process.stderr.write;

  const originalCwd = process.cwd();
  process.exitCode = 0;
  try {
    process.chdir(cwd);
    await exploreCommand(argv);
  } finally {
    process.chdir(originalCwd);
    for (const [key, value] of previousEnv.entries()) {
      if (value === undefined) delete process.env[key];
      else process.env[key] = value;
    }
    process.stdout.write = originalStdout;
    process.stderr.write = originalStderr;
  }

  const exitCode = process.exitCode ?? 0;
  process.exitCode = originalExitCode;
  return { stdout: stdoutChunks.join(''), stderr: stderrChunks.join(''), exitCode };
}