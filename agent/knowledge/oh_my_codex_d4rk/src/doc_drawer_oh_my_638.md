vedWatcher(cwd: string): Promise<void> {
  if (process.env.OMX_HOOK_DERIVED_SIGNALS !== "1") return;

  const { mkdir, writeFile, readFile } = await import("fs/promises");
  const pidPath = hookDerivedWatcherPidPath(cwd);
  const pkgRoot = getPackageRoot();
  const watcherScript = resolveHookDerivedWatcherScript(pkgRoot);
  if (!existsSync(watcherScript)) return;

  if (existsSync(pidPath)) {
    try {
      const prev = JSON.parse(await readFile(pidPath, "utf-8")) as {
        pid?: number;
      };
      if (prev && typeof prev.pid === "number") {
        process.kill(prev.pid, "SIGTERM");
      }
    } catch (error: unknown) {
      console.warn("[omx] warning: failed to stop stale hook-derived watcher", {
        path: pidPath,