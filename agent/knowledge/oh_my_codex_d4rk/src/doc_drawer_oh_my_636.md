ACK_MAX_LIFETIME_MS
        ? ["--max-lifetime-ms", process.env.OMX_NOTIFY_FALLBACK_MAX_LIFETIME_MS]
        : []),
    ],
    {
      cwd,
      detached: true,
      stdio: "ignore",
      env: buildNotifyFallbackWatcherEnv(process.env, {
        codexHomeOverride: options.codexHomeOverride,
        enableAuthority: options.enableAuthority === true,
        sessionId: options.sessionId,
      }),
    },
  );
  child.unref();