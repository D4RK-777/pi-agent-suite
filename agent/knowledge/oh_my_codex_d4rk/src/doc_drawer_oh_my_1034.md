se {
    if (options.verbose) console.log("  No OMX config entries found.");
  }

  return result;
}

async function removeInstalledPrompts(
  promptsDir: string,
  pkgRoot: string,
  options: Pick<UninstallOptions, "dryRun" | "verbose">,
): Promise<number> {
  const srcPromptsDir = join(pkgRoot, "prompts");
  if (!existsSync(srcPromptsDir) || !existsSync(promptsDir)) return 0;

  let removed = 0;
  const sourceFiles = await readdir(srcPromptsDir);

  for (const file of sourceFiles) {
    if (!file.endsWith(".md")) continue;
    const installed = join(promptsDir, file);
    if (!existsSync(installed)) continue;