e.active) {
          state.active = false;
          state.completed_at = new Date().toISOString();
          await writeFile(path, JSON.stringify(state, null, 2));
        }
      }
    }
  } catch (err) {
    console.error(
      `[omx] postLaunch: mode cleanup failed: ${err instanceof Error ? err.message : err}`,
    );
  }

  // 4. Send session-end lifecycle notification (best effort)
  try {
    const { notifyLifecycle } = await import("../notifications/index.js");
    const durationMs = sessionStartedAt
      ? Date.now() - new Date(sessionStartedAt).getTime()
      : undefined;
    await notifyLifecycle("session-end", {
      sessionId,
      projectPath: cwd,
      projectName: basename(cwd),
      durationMs,
      reason: "session_exit",
    });
  } catch (err) {