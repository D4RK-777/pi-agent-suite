anonical ${overlap.canonicalDir}; remove or archive it if Codex shows duplicate entries`,
    };
  }

  const mismatchMessage = overlap.mismatchedSkillNames.length > 0
    ? `; ${overlap.mismatchedSkillNames.length} differ in SKILL.md content`
    : '';
  return {
    name: 'Legacy skill roots',
    status: 'warn',
    message:
      `${overlap.overlappingSkillNames.length} overlapping skill names between ${overlap.canonicalDir} and ${overlap.legacyDir}${mismatchMessage}; Codex Enable/Disable Skills may show duplicates until ~/.agents/skills is cleaned up`,
  };
}