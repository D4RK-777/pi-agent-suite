x] operation failed: ${err}\n`);
    // Non-fatal: notification failures must never block launch
  }

  // 6. Dispatch native hook event (best effort)
  try {
    await emitNativeHookEvent(cwd, "session-start", {
      session_id: sessionId,
      context: buildNativeHookBaseContext(cwd, sessionId, "started", {
        project_path: cwd,
        project_name: basename(cwd),
        status: "started",
      }),
    });
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }
}