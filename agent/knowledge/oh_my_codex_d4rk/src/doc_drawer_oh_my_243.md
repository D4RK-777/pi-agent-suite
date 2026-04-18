ry, `agents[${index}].category`);
    assertNonEmptyString(entry.status, `agents[${index}].status`);

    if (!AGENT_CATEGORIES.has(entry.category as CatalogAgentCategory)) {
      throw new Error(`catalog_manifest_invalid:agents[${index}].category`);
    }
    if (!ENTRY_STATUSES.has(entry.status as CatalogEntryStatus)) {
      throw new Error(`catalog_manifest_invalid:agents[${index}].status`);
    }

    const name = entry.name.trim();
    if (seenAgents.has(name)) throw new Error(`catalog_manifest_invalid:duplicate_agent:${name}`);
    seenAgents.add(name);

    const canonical = typeof entry.canonical === 'string' && entry.canonical.trim() !== ''
      ? entry.canonical.trim()
      : undefined;