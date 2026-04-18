{
        console.log(`[omx] ${info}`);
      }
      for (const warning of startup.warningLines) {
        console.warn(`[omx] ${warning}`);
      }
    } else {
      delete process.env[OMX_NOTIFY_TEMP_CONTRACT_ENV];
    }
    const { notifyLifecycle } = await import("../notifications/index.js");
    await notifyLifecycle("session-start", {
      sessionId,
      projectPath: cwd,
      projectName: basename(cwd),
    });
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal: notification failures must never block launch
  }