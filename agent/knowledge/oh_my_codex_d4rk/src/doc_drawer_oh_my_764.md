ummary> {
  const summary = createEmptyCategorySummary();
  if (!existsSync(srcDir)) return summary;

  const manifest = tryReadCatalogManifest();
  const agentStatusByName = manifest
    ? new Map(manifest.agents.map((agent) => [agent.name, agent.status]))
    : null;
  const isInstallableStatus = (status: string | undefined): boolean =>
    status === "active" || status === "internal";

  const files = await readdir(srcDir);
  const staleCandidatePromptNames = new Set(
    manifest?.agents.map((agent) => agent.name) ?? [],
  );

  for (const file of files) {
    if (!file.endsWith(".md")) continue;
    const promptName = file.slice(0, -3);
    staleCandidatePromptNames.add(promptName);