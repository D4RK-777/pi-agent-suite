ASK_ORIGINAL_TASK_ENV]: parsed.prompt,
      },
      stdio: ['ignore', 'pipe', 'pipe'],
    },
  );

  if (child.stdout && child.stdout.length > 0) {
    process.stdout.write(child.stdout);
  }
  if (child.stderr && child.stderr.length > 0) {
    process.stderr.write(child.stderr);
  }

  if (child.error) {
    throw new Error(`[ask] failed to launch advisor script: ${child.error.message}`);
  }

  const status = typeof child.status === 'number'
    ? child.status
    : resolveSignalExitCode(child.signal);

  if (status !== 0) {
    process.exitCode = status;
  }
}