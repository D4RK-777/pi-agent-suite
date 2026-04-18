ck<SetupOptions, "dryRun" | "verbose">,
): Promise<number> {
  if (!existsSync(agentsDir)) return 0;

  const installedFiles = await readdir(agentsDir);
  let removed = 0;

  for (const file of installedFiles) {
    if (!file.endsWith(".toml")) continue;

    const fullPath = join(agentsDir, file);
    let content = "";
    try {
      content = await readFile(fullPath, "utf-8");
    } catch {
      continue;
    }

    if (!containsTomlKey(content, OBSOLETE_NATIVE_AGENT_FIELD)) continue;