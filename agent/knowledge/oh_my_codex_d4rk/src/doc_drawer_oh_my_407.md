omptCount - SAFETY_BUFFER),
    skillMin: Math.max(1, installableSkillCount - SAFETY_BUFFER),
  };
}

export function getCatalogHeadlineCounts(): { prompts: number; skills: number } | null {
  const manifest = tryReadCatalogManifest();
  if (!manifest) return null;
  return {
    prompts: countInstallablePrompts(manifest),
    skills: countInstallableSkills(manifest),
  };
}