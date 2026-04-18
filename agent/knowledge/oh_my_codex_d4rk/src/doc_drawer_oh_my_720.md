th roots; archive or remove ~/.agents/skills if Enable/Disable Skills shows duplicates.`,
    };
  }

  const mismatchSuffix = overlap.mismatchedSkillNames.length > 0
    ? ` ${overlap.mismatchedSkillNames.length} overlapping skills have different SKILL.md content.`
    : "";
  return {
    shouldWarn: true,
    message:
      `Detected ${overlap.overlappingSkillNames.length} overlapping skill names between canonical ${overlap.canonicalDir} and legacy ${overlap.legacyDir}.${mismatchSuffix} Remove or archive ~/.agents/skills after confirming ${overlap.canonicalDir} is the version you want Codex to load.`,
  };
}