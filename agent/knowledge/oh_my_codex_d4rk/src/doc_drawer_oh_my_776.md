eStatus = (status: string | undefined): boolean =>
    status === "active" || status === "internal";
  const entries = await readdir(srcDir, { withFileTypes: true });
  const staleCandidateSkillNames = new Set(
    manifest?.skills.map((skill) => skill.name) ?? [],
  );
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    staleCandidateSkillNames.add(entry.name);
    const status = skillStatusByName?.get(entry.name);
    if (skillStatusByName && !isInstallableStatus(status)) {
      summary.skipped += 1;
      if (options.verbose) {
        const label = status ?? "unlisted";
        console.log(`  skipped ${entry.name}/ (status: ${label})`);
      }
      continue;
    }