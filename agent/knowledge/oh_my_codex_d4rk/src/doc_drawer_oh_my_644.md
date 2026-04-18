Path,
        error: error instanceof Error ? error.message : String(error),
      },
    );
  });
}

async function flushNotifyFallbackOnce(
  cwd: string,
  options: { codexHomeOverride?: string; enableAuthority?: boolean; sessionId?: string } = {},
): Promise<void> {
  const { spawnSync } = await import("child_process");
  const pkgRoot = getPackageRoot();
  const watcherScript = resolveNotifyFallbackWatcherScript(pkgRoot);
  const notifyScript = resolveNotifyHookScript(pkgRoot);
  if (!existsSync(watcherScript) || !existsSync(notifyScript)) return;
  spawnSync(
    process.execPath,
    [watcherScript, "--once", "--cwd", cwd, "--notify-script", notifyScript],
    {
      cwd,
      stdio: "ignore",
      timeout: 3000,
      env: buildNotifyFallbackWatcherEnv(process.env, {