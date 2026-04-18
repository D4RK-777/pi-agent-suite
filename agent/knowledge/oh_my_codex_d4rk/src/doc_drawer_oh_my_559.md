it repairConfigIfNeeded(
      codexConfigPath(),
      getPackageRoot(),
    );
    if (repaired) {
      console.log("[omx] Repaired duplicate [tui] section in config.toml.");
    }
  } catch {
    // Non-fatal: repair failure must not block launch
  }

  // ── Phase 1: preLaunch ──────────────────────────────────────────────────
  try {
    await preLaunch(cwd, sessionId, notifyTempResult.contract, codexHomeOverride, enableNotifyFallbackAuthority);
  } catch (err) {
    // preLaunch errors must NOT prevent Codex from starting
    console.error(
      `[omx] preLaunch warning: ${err instanceof Error ? err.message : err}`,
    );
  }