rojectRoot)
      : null;
  const sessionIsActive = activeSession && !isSessionStale(activeSession);

  if (existsSync(agentsMdSrc)) {
    const content = await readFile(agentsMdSrc, "utf-8");
    const modelTableContext = resolveAgentsModelTableContext(resolvedConfig, {
      codexHomeOverride: scopeDirs.codexHomeDir,
    });
    const rewritten = upsertAgentsModelTable(
      addGeneratedAgentsMarker(
        applyScopePathRewritesToAgentsTemplate(content, resolvedScope.scope),
      ),
      modelTableContext,
    );
    let changed = true;
    let canApplyManagedModelRefresh = false;
    let managedRefreshContent = "";
    if (agentsMdExists) {
      const existing = await readFile(agentsMdDst, "utf-8");
      changed = existing !== rewritten;