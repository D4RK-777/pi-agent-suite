rt("fs/promises");
  const pidPath = notifyFallbackPidPath(cwd);
  if (!existsSync(pidPath)) return;

  try {
    const pid = parseWatcherPidFile(await readFile(pidPath, "utf-8"));
    if (pid) {
      tryKillPid(pid, "SIGTERM");
    }
  } catch (error: unknown) {
    if (!hasErrnoCode(error, "ESRCH")) {
      console.warn(
        "[omx] warning: failed to stop notify fallback watcher process",
        {
          path: pidPath,
          error: error instanceof Error ? error.message : String(error),
        },
      );
    }
  }