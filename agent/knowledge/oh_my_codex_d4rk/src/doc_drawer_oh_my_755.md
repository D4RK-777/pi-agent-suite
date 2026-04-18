the full skill instructions at\s+.*\/skills\/[^/\s]+\/SKILL\.md/i;
  return marker.test(content);
}

async function cleanupLegacySkillPromptShims(
  promptsSrcDir: string,
  promptsDstDir: string,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
): Promise<number> {
  if (!existsSync(promptsSrcDir) || !existsSync(promptsDstDir)) return 0;

  const sourceFiles = new Set(
    (await readdir(promptsSrcDir)).filter((name) => name.endsWith(".md")),
  );

  const installedFiles = await readdir(promptsDstDir);
  let removed = 0;

  for (const file of installedFiles) {
    if (!file.endsWith(".md")) continue;
    if (sourceFiles.has(file)) continue;