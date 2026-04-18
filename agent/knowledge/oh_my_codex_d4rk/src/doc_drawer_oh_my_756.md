installedFiles) {
    if (!file.endsWith(".md")) continue;
    if (sourceFiles.has(file)) continue;

    const fullPath = join(promptsDstDir, file);
    let content = "";
    try {
      content = await readFile(fullPath, "utf-8");
    } catch {
      continue;
    }

    if (!isLegacySkillPromptShim(content)) continue;

    if (!options.dryRun) {
      await rm(fullPath, { force: true });
    }
    if (options.verbose) console.log(`  removed legacy prompt shim ${file}`);
    removed++;
  }

  return removed;
}

function isGitHubCliConfigured(): boolean {
  const result = spawnSync("gh", ["auth", "status"], { stdio: "ignore",
      windowsHide: true,
    });
  return result.status === 0;
}