}

  const catalogCounts = getCatalogHeadlineCounts();
  const summary = createEmptyRunSummary();

  // Step 2: Install agent prompts
  console.log("[2/8] Installing agent prompts...");
  {
    const promptsSrc = join(pkgRoot, "prompts");
    const promptsDst = scopeDirs.promptsDir;
    summary.prompts = await installPrompts(
      promptsSrc,
      promptsDst,
      backupContext,
      { force, dryRun, verbose },
    );
    const cleanedLegacyPromptShims = await cleanupLegacySkillPromptShims(
      promptsSrc,
      promptsDst,
      {
        dryRun,
        verbose,
      },
    );
    summary.prompts.removed += cleanedLegacyPromptShims;
    if (cleanedLegacyPromptShims > 0) {
      if (dryRun) {
        console.log(