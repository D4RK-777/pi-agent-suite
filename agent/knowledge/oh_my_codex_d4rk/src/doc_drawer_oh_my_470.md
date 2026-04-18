kill roots',
      status: 'pass',
      message: 'no ~/.agents/skills overlap detected',
    };
  }

  if (overlap.sameResolvedTarget) {
    return {
      name: 'Legacy skill roots',
      status: 'pass',
      message:
        `~/.agents/skills links to canonical ${overlap.canonicalDir}; treating both paths as one shared skill root`,
    };
  }

  if (overlap.overlappingSkillNames.length === 0) {
    return {
      name: 'Legacy skill roots',
      status: 'warn',
      message:
        `legacy ~/.agents/skills still exists (${overlap.legacySkillCount} skills) alongside canonical ${overlap.canonicalDir}; remove or archive it if Codex shows duplicate entries`,
    };
  }