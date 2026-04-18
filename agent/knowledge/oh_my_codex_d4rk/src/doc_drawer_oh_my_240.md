ry, `skills[${index}].category`);
    assertNonEmptyString(entry.status, `skills[${index}].status`);

    if (!SKILL_CATEGORIES.has(entry.category as CatalogSkillCategory)) {
      throw new Error(`catalog_manifest_invalid:skills[${index}].category`);
    }
    if (!ENTRY_STATUSES.has(entry.status as CatalogEntryStatus)) {
      throw new Error(`catalog_manifest_invalid:skills[${index}].status`);
    }

    const name = entry.name.trim();
    if (seenSkills.has(name)) throw new Error(`catalog_manifest_invalid:duplicate_skill:${name}`);
    seenSkills.add(name);

    const canonical = typeof entry.canonical === 'string' && entry.canonical.trim() !== ''
      ? entry.canonical.trim()
      : undefined;