const status = skillStatusByName?.get(staleSkill);
      if (isInstallableStatus(status)) continue;

      const staleSkillDir = join(dstDir, staleSkill);
      if (!existsSync(staleSkillDir)) continue;

      if (!options.dryRun) {
        await rm(staleSkillDir, { recursive: true, force: true });
      }
      summary.removed += 1;
      if (options.verbose) {
        const prefix = options.dryRun
          ? "would remove stale skill"
          : "removed stale skill";
        const label = status ?? "unlisted";
        console.log(`  ${prefix} ${staleSkill}/ (status: ${label})`);
      }
    }
  }

  return summary;
}