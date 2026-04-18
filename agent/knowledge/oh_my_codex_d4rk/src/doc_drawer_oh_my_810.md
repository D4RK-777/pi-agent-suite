)`);
    }
    throw new Error(`[sparkshell] failed to launch native binary: ${errno.message}`);
  }

  if (!hasExplicitOverride && isSparkShellNativeCompatibilityFailure(result)) {
    process.stderr.write('[sparkshell] GLIBC-incompatible native sidecar detected; falling back to raw command execution without summary support.\n');
    runSparkShellFallback(args, { announce: false });
    return;
  }

  writeSparkShellResultOutput(result);

  if (result.status !== 0) {
    process.exitCode = typeof result.status === 'number'
      ? result.status
      : resolveSignalExitCode(result.signal);
  }
}