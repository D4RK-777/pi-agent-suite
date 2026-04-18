tch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }

  // 5. Emit temp notification startup summary + warnings, then send session-start lifecycle notification (best effort)
  try {
    if (notifyTempContract?.active) {
      process.env[OMX_NOTIFY_TEMP_CONTRACT_ENV] =
        serializeNotifyTempContract(notifyTempContract);
      const { getNotificationConfig } =
        await import("../notifications/config.js");
      const resolved = getNotificationConfig();
      const startup = buildNotifyTempStartupMessages(
        notifyTempContract,
        Boolean(resolved?.enabled),
      );
      for (const info of startup.infoLines) {
        console.log(`[omx] ${info}`);
      }
      for (const warning of startup.warningLines) {