ical === 'string' && entry.canonical.trim() !== ''
      ? entry.canonical.trim()
      : undefined;

    if ((entry.status === 'alias' || entry.status === 'merged') && !canonical) {
      throw new Error(`catalog_manifest_invalid:skills[${index}].canonical`);
    }

    return {
      name,
      category: entry.category as CatalogSkillCategory,
      status: entry.status as CatalogEntryStatus,
      canonical,
      core: entry.core === true,
      internalRequired: entry.internalRequired === true,
    };
  });