: undefined;
    await emitNativeHookEvent(cwd, "session-end", {
      session_id: sessionId,
      context: buildNativeHookBaseContext(cwd, sessionId, normalizedEvent, {
        project_path: cwd,
        project_name: basename(cwd),
        duration_ms: durationMs,
        reason: "session_exit",
        status: normalizedEvent === "failed" ? "failed" : "finished",
        ...(process.exitCode !== undefined
          ? { exit_code: process.exitCode }
          : {}),
        ...(errorSummary ? { error_summary: errorSummary } : {}),
      }),
    });
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }
}