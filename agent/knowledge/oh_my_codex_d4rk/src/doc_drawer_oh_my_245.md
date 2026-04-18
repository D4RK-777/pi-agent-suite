ive') {
      throw new Error(`catalog_manifest_invalid:missing_core_skill:${coreSkill}`);
    }
  }

  return {
    schemaVersion: input.schemaVersion,
    catalogVersion: input.catalogVersion,
    skills,
    agents,
  };
}

export interface CatalogCounts {
  skillCount: number;
  promptCount: number;
  activeSkillCount: number;
  activeAgentCount: number;
}

export function summarizeCatalogCounts(manifest: CatalogManifest): CatalogCounts {
  return {
    skillCount: manifest.skills.length,
    promptCount: manifest.agents.length,
    activeSkillCount: manifest.skills.filter((s) => s.status === 'active').length,
    activeAgentCount: manifest.agents.filter((a) => a.status === 'active').length,
  };
}