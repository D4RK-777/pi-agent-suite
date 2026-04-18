nifest_invalid:schemaVersion');
  }

  assertNonEmptyString(input.catalogVersion, 'catalogVersion');

  if (!Array.isArray(input.skills)) throw new Error('catalog_manifest_invalid:skills');
  if (!Array.isArray(input.agents)) throw new Error('catalog_manifest_invalid:agents');

  const seenSkills = new Set<string>();
  const skills: CatalogSkillEntry[] = input.skills.map((entry, index) => {
    if (!isObject(entry)) throw new Error(`catalog_manifest_invalid:skills[${index}]`);
    assertNonEmptyString(entry.name, `skills[${index}].name`);
    assertNonEmptyString(entry.category, `skills[${index}].category`);
    assertNonEmptyString(entry.status, `skills[${index}].status`);