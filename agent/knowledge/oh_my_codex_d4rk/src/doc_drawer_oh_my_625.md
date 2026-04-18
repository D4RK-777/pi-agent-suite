tch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }

  // 1. Remove session-scoped model instructions file
  try {
    await removeSessionModelInstructionsFile(cwd, sessionId);
  } catch (err) {
    console.error(
      `[omx] postLaunch: model instructions cleanup failed: ${err instanceof Error ? err.message : err}`,
    );
  }

  // 2. Archive session (write history, delete session.json)
  try {
    await writeSessionEnd(cwd, sessionId);
  } catch (err) {
    console.error(
      `[omx] postLaunch: session archive failed: ${err instanceof Error ? err.message : err}`,
    );
  }