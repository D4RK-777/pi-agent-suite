nternalHidden = manifest.skills
    .filter((s) => s.status === 'internal')
    .map((s) => s.name);

  return {
    generatedAt: new Date().toISOString(),
    version: manifest.catalogVersion,
    counts: summarizeCatalogCounts(manifest),
    coreSkills: manifest.skills.filter((s) => s.core).map((s) => s.name),
    skills: manifest.skills,
    agents: manifest.agents,
    aliases,
    internalHidden,
  };
}