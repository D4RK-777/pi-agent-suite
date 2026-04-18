ical === 'string' && entry.canonical.trim() !== ''
      ? entry.canonical.trim()
      : undefined;

    if ((entry.status === 'alias' || entry.status === 'merged') && !canonical) {
      throw new Error(`catalog_manifest_invalid:agents[${index}].canonical`);
    }

    return {
      name,
      category: entry.category as CatalogAgentCategory,
      status: entry.status as CatalogEntryStatus,
      canonical,
    };
  });

  for (const coreSkill of REQUIRED_CORE_SKILLS) {
    const skill = skills.find((s) => s.name === coreSkill);
    if (!skill || skill.status !== 'active') {
      throw new Error(`catalog_manifest_invalid:missing_core_skill:${coreSkill}`);
    }
  }