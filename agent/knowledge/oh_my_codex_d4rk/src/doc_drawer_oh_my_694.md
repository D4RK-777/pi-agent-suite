? [],
    ...(artifacts.canonicalPrdPath ? { canonical_prd_path: artifacts.canonicalPrdPath } : {}),
  });
  if (artifacts.migratedPrd) {
    console.log('[ralph] Migrated legacy PRD -> ' + artifacts.canonicalPrdPath);
  }
  if (artifacts.migratedProgress) {
    console.log('[ralph] Migrated legacy progress -> ' + artifacts.canonicalProgressPath);
  }
  console.log('[ralph] Ralph persistence mode active. Launching Codex...');
  console.log(`[ralph] available_agent_types: ${staffingPlan.rosterSummary}`);
  console.log(`[ralph] staffing_plan: ${staffingPlan.staffingSummary}`);
  const { launchWithHud } = await import('./index.js');
  const codexArgsBase = filterRalphCodexArgs(normalizedArgs);
  const codexArgs = explicitTask === 'ralph-cli-launch' && approvedHint?.task