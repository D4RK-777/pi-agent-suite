cySkillOverlapNotice> {
  if (scope !== "user") {
    return { shouldWarn: false, message: "" };
  }

  const overlap = await detectLegacySkillRootOverlap();
  if (!overlap.legacyExists) {
    return { shouldWarn: false, message: "" };
  }

  if (overlap.overlappingSkillNames.length === 0) {
    return {
      shouldWarn: true,
      message:
        `Legacy ~/.agents/skills still exists (${overlap.legacySkillCount} skills) alongside canonical ${overlap.canonicalDir}. Codex may still discover both roots; archive or remove ~/.agents/skills if Enable/Disable Skills shows duplicates.`,
    };
  }