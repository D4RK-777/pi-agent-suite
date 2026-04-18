console.warn("[omx] warning: failed to stop stale hook-derived watcher", {
        path: pidPath,
        error: error instanceof Error ? error.message : String(error),
      });
    }
  }

  await mkdir(join(cwd, ".omx", "state"), { recursive: true }).catch(
    (error: unknown) => {
      console.warn(
        "[omx] warning: failed to create hook-derived watcher state directory",
        {
          cwd,
          error: error instanceof Error ? error.message : String(error),
        },
      );
    },
  );
  const child = spawn(process.execPath, [watcherScript, "--cwd", cwd], {
    cwd,
    detached: true,
    stdio: "ignore",
    env: process.env,
  });
  child.unref();