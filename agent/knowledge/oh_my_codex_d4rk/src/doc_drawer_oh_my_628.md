rojectName: basename(cwd),
      durationMs,
      reason: "session_exit",
    });
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal: notification failures must never block session cleanup
  }

  // 5. Dispatch native hook event (best effort)
  try {
    const durationMs = sessionStartedAt
      ? Date.now() - new Date(sessionStartedAt).getTime()
      : undefined;
    const normalizedEvent =
      process.exitCode && process.exitCode !== 0 ? "failed" : "finished";
    const errorSummary =
      normalizedEvent === "failed"
        ? `codex exited with code ${process.exitCode}`
        : undefined;
    await emitNativeHookEvent(cwd, "session-end", {
      session_id: sessionId,