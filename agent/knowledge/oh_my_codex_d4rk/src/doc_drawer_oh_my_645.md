stdio: "ignore",
      timeout: 3000,
      env: buildNotifyFallbackWatcherEnv(process.env, {
        codexHomeOverride: options.codexHomeOverride,
        enableAuthority: options.enableAuthority === true,
        sessionId: options.sessionId,
      }),
    },
  );
}

async function flushHookDerivedWatcherOnce(cwd: string): Promise<void> {
  if (process.env.OMX_HOOK_DERIVED_SIGNALS !== "1") return;
  const { spawnSync } = await import("child_process");
  const pkgRoot = getPackageRoot();
  const watcherScript = resolveHookDerivedWatcherScript(pkgRoot);
  if (!existsSync(watcherScript)) return;
  spawnSync(process.execPath, [watcherScript, "--once", "--cwd", cwd], {
    cwd,
    stdio: "ignore",
    timeout: 3000,
    env: {
      ...process.env,