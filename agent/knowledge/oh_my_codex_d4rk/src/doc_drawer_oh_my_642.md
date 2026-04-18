error: error instanceof Error ? error.message : String(error),
        },
      );
    }
  }

  await unlink(pidPath).catch((error: unknown) => {
    console.warn(
      "[omx] warning: failed to remove notify fallback watcher pid file",
      {
        path: pidPath,
        error: error instanceof Error ? error.message : String(error),
      },
    );
  });
}

async function stopHookDerivedWatcher(cwd: string): Promise<void> {
  const { readFile, unlink } = await import("fs/promises");
  const pidPath = hookDerivedWatcherPidPath(cwd);
  if (!existsSync(pidPath)) return;