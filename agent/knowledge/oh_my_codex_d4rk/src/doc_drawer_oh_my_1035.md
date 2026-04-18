)) continue;
    const installed = join(promptsDir, file);
    if (!existsSync(installed)) continue;

    if (!options.dryRun) {
      await rm(installed, { force: true });
    }
    if (options.verbose)
      console.log(
        `  ${options.dryRun ? "Would remove" : "Removed"} prompt: ${file}`,
      );
    removed++;
  }

  return removed;
}

async function removeInstalledSkills(
  skillsDir: string,
  pkgRoot: string,
  options: Pick<UninstallOptions, "dryRun" | "verbose">,
): Promise<number> {
  const srcSkillsDir = join(pkgRoot, "skills");
  if (!existsSync(srcSkillsDir) || !existsSync(skillsDir)) return 0;

  let removed = 0;
  const sourceEntries = await readdir(srcSkillsDir, { withFileTypes: true });