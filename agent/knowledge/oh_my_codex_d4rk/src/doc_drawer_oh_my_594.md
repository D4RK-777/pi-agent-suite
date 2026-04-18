ON_ID: options.sessionId } : {}),
    OMX_HUD_AUTHORITY: options.enableAuthority ? "1" : "0",
  };
}

/**
 * preLaunch: Prepare environment before Codex starts.
 * 1. Generate runtime overlay + write session-scoped model instructions file
 * 2. Write session.json
 *
 * Automatic stale-session cleanup is intentionally disabled here. Destructive
 * cleanup must be explicit via `omx cleanup` so normal launches never reap
 * files or processes from other OMX sessions.
 */
async function preLaunch(
  cwd: string,
  sessionId: string,
  notifyTempContract?: NotifyTempContract,
  codexHomeOverride?: string,
  enableNotifyFallbackAuthority: boolean = false,
): Promise<void> {
  // 1. Generate runtime overlay + write session-scoped model instructions file