r: error instanceof Error ? error.message : String(error),
          },
        );
      }
    }
  }

  await mkdir(join(cwd, ".omx", "state"), { recursive: true }).catch(
    (error: unknown) => {
      console.warn(
        "[omx] warning: failed to create notify fallback watcher state directory",
        {
          cwd,
          error: error instanceof Error ? error.message : String(error),
        },
      );
    },
  );
  const child = spawn(
    process.execPath,
    [
      watcherScript,
      "--cwd",
      cwd,
      "--notify-script",
      notifyScript,
      "--pid-file",
      pidPath,
      "--parent-pid",
      String(process.pid),
      ...(process.env.OMX_NOTIFY_FALLBACK_MAX_LIFETIME_MS
        ? ["--max-lifetime-ms", process.env.OMX_NOTIFY_FALLBACK_MAX_LIFETIME_MS]