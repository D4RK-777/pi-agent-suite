bose" | "force">,
): Promise<SetupCategorySummary> {
  const summary = createEmptyCategorySummary();

  if (!options.dryRun) {
    await mkdir(agentsDir, { recursive: true });
  }

  const manifest = tryReadCatalogManifest();
  const agentStatusByName = manifest
    ? new Map(manifest.agents.map((agent) => [agent.name, agent.status]))
    : null;
  const isInstallableStatus = (status: string | undefined): boolean =>
    status === "active" || status === "internal";
  const staleCandidateNativeAgentNames = new Set(
    manifest?.agents.map((agent) => agent.name) ?? [],
  );