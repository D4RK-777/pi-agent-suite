cli/index] operation failed: ${err}\n`);
    // Non-fatal: update checks must never block launch
  }

  try {
    await maybePromptGithubStar();
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal: star prompt must never block launch
  }

  // ── Phase 0.5: config repair ────────────────────────────────────────────
  // After an omx version upgrade the OLD setup code (still in memory) may
  // have written a config.toml with duplicate [tui] sections.  Codex CLI's
  // TOML parser rejects duplicates, so we repair before spawning the CLI.
  try {
    const repaired = await repairConfigIfNeeded(
      codexConfigPath(),
      getPackageRoot(),
    );
    if (repaired) {