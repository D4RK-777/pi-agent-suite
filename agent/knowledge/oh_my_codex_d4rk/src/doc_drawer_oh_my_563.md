hubStar();
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
  }

  try {
    const repaired = await repairConfigIfNeeded(
      codexConfigPath(),
      getPackageRoot(),
    );
    if (repaired) {
      console.log("[omx] Repaired duplicate [tui] section in config.toml.");
    }
  } catch {
    // Non-fatal
  }

  try {
    await preLaunch(cwd, sessionId, notifyTempResult.contract, codexHomeOverride, true);
  } catch (err) {
    console.error(
      `[omx] preLaunch warning: ${err instanceof Error ? err.message : err}`,
    );
  }