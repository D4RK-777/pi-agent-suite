.destinationDir;

    if (!options.dryRun) {
      await mkdir(skillDst, { recursive: true });
    }

    const skillFiles = await readdir(skillSrc);
    for (const sf of skillFiles) {
      const sfPath = join(skillSrc, sf);
      const sfStat = await stat(sfPath);
      if (!sfStat.isFile()) continue;
      const dstPath = join(skillDst, sf);
      await syncManagedFileFromDisk(
        sfPath,
        dstPath,
        summary,
        backupContext,
        options,
        `skill ${skillName}/${sf}`,
      );
    }
  }

  if (options.force && manifest && existsSync(dstDir)) {
    for (const staleSkill of staleCandidateSkillNames) {
      const status = skillStatusByName?.get(staleSkill);
      if (isInstallableStatus(status)) continue;