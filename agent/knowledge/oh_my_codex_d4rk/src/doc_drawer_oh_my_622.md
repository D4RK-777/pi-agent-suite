detached: true,
      stdio: "ignore",
      windowsHide: true,
    },
  );
  child.unref();
}

/**
 * postLaunch: Clean up after Codex exits.
 * Each step is independently fault-tolerant (try/catch per step).
 */
async function postLaunch(
  cwd: string,
  sessionId: string,
  codexHomeOverride?: string,
  enableNotifyFallbackAuthority: boolean = false,
): Promise<void> {
  // Capture session start time before cleanup (writeSessionEnd deletes session.json)
  let sessionStartedAt: string | undefined;
  try {
    const sessionState = await readSessionState(cwd);
    sessionStartedAt = sessionState?.started_at;
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }