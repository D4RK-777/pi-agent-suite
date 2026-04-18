d], {
    cwd,
    detached: true,
    stdio: "ignore",
    env: process.env,
  });
  child.unref();

  await writeFile(
    pidPath,
    JSON.stringify(
      { pid: child.pid, started_at: new Date().toISOString() },
      null,
      2,
    ),
  ).catch((error: unknown) => {
    console.warn(
      "[omx] warning: failed to write hook-derived watcher pid file",
      {
        path: pidPath,
        error: error instanceof Error ? error.message : String(error),
      },
    );
  });
}

async function stopNotifyFallbackWatcher(cwd: string): Promise<void> {
  const { readFile, unlink } = await import("fs/promises");
  const pidPath = notifyFallbackPidPath(cwd);
  if (!existsSync(pidPath)) return;