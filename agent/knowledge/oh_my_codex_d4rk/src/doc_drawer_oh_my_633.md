sessionId?: string } = {},
): Promise<void> {
  if (process.env.OMX_NOTIFY_FALLBACK === "0") return;

  const { mkdir, writeFile, readFile } = await import("fs/promises");
  const pidPath = notifyFallbackPidPath(cwd);
  const pkgRoot = getPackageRoot();
  const watcherScript = resolveNotifyFallbackWatcherScript(pkgRoot);
  const notifyScript = resolveNotifyHookScript(pkgRoot);
  if (!existsSync(watcherScript) || !existsSync(notifyScript)) return;