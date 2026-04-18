lveNotifyHookScript(pkgRoot);
  if (!existsSync(watcherScript) || !existsSync(notifyScript)) return;

  // Stop stale watcher from a previous run.
  if (existsSync(pidPath)) {
    try {
      const prevPid = parseWatcherPidFile(await readFile(pidPath, "utf-8"));
      if (prevPid) {
        tryKillPid(prevPid, "SIGTERM");
      }
    } catch (error: unknown) {
      if (!hasErrnoCode(error, "ESRCH")) {
        console.warn(
          "[omx] warning: failed to stop stale notify fallback watcher",
          {
            path: pidPath,
            error: error instanceof Error ? error.message : String(error),
          },
        );
      }
    }
  }