sole.error(
      `[omx] preLaunch warning: ${err instanceof Error ? err.message : err}`,
    );
  }

  // ── Phase 2: run ────────────────────────────────────────────────────────
  try {
    const notifyTempContractRaw = notifyTempResult.contract.active
      ? serializeNotifyTempContract(notifyTempResult.contract)
      : null;
    runCodex(
      cwd,
      normalizedArgs,
      sessionId,
      workerSparkModel,
      codexHomeOverride,
      notifyTempContractRaw,
    );
  } finally {
    // ── Phase 3: postLaunch ─────────────────────────────────────────────
    await postLaunch(cwd, sessionId, codexHomeOverride, enableNotifyFallbackAuthority);
  }
}