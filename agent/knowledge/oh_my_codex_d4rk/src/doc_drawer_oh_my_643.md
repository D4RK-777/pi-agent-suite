fs/promises");
  const pidPath = hookDerivedWatcherPidPath(cwd);
  if (!existsSync(pidPath)) return;

  try {
    const parsed = JSON.parse(await readFile(pidPath, "utf-8")) as {
      pid?: number;
    };
    if (parsed && typeof parsed.pid === "number") {
      process.kill(parsed.pid, "SIGTERM");
    }
  } catch (error: unknown) {
    console.warn("[omx] warning: failed to stop hook-derived watcher process", {
      path: pidPath,
      error: error instanceof Error ? error.message : String(error),
    });
  }

  await unlink(pidPath).catch((error: unknown) => {
    console.warn(
      "[omx] warning: failed to remove hook-derived watcher pid file",
      {
        path: pidPath,
        error: error instanceof Error ? error.message : String(error),
      },
    );
  });
}