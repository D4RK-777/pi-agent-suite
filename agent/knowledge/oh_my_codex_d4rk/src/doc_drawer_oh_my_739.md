ts.prompts}).\n`,
      );
    } else {
      console.log("  Prompt refresh complete.\n");
    }
  }

  // Step 3: Install skills
  console.log("[3/8] Installing skills...");
  {
    const skillsSrc = join(pkgRoot, "skills");
    const skillsDst = scopeDirs.skillsDir;
    summary.skills = await installSkills(skillsSrc, skillsDst, backupContext, {
      force,
      dryRun,
      verbose,
    });
    if (catalogCounts) {
      console.log(
        `  Skill refresh complete (catalog baseline: ${catalogCounts.skills}).\n`,
      );
    } else {
      console.log("  Skill refresh complete.\n");
    }
  }