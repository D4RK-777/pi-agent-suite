ableAuthority === true,
        sessionId: options.sessionId,
      }),
    },
  );
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
      "[omx] warning: failed to write notify fallback watcher pid file",
      {
        path: pidPath,
        error: error instanceof Error ? error.message : String(error),
      },
    );
  });
}

async function startHookDerivedWatcher(cwd: string): Promise<void> {
  if (process.env.OMX_HOOK_DERIVED_SIGNALS !== "1") return;