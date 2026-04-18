";
        console.log(`  skipped ${entry.name}/ (status: ${label})`);
      }
      continue;
    }

    const skillSrc = join(srcDir, entry.name);
    const skillDst = join(dstDir, entry.name);
    const skillMd = join(skillSrc, "SKILL.md");
    if (!existsSync(skillMd)) continue;

    installableSkills.push({
      name: entry.name,
      sourceDir: skillSrc,
      destinationDir: skillDst,
    });
  }

  for (const skill of installableSkills) {
    await validateSkillFile(join(skill.sourceDir, "SKILL.md"));
  }

  for (const skill of installableSkills) {
    const skillName = skill.name;
    const skillSrc = skill.sourceDir;
    const skillDst = skill.destinationDir;

    if (!options.dryRun) {
      await mkdir(skillDst, { recursive: true });
    }