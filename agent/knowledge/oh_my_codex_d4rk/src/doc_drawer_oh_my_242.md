core: entry.core === true,
      internalRequired: entry.internalRequired === true,
    };
  });

  const seenAgents = new Set<string>();
  const agents: CatalogAgentEntry[] = input.agents.map((entry, index) => {
    if (!isObject(entry)) throw new Error(`catalog_manifest_invalid:agents[${index}]`);
    assertNonEmptyString(entry.name, `agents[${index}].name`);
    assertNonEmptyString(entry.category, `agents[${index}].category`);
    assertNonEmptyString(entry.status, `agents[${index}].status`);