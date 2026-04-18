ills
    .filter((skill) => skill.status === 'active' || skill.status === 'internal')
    .length;
}

export function getCatalogExpectations(): CatalogExpectations {
  const manifest = tryReadCatalogManifest();
  if (!manifest) {
    return { promptMin: 25, skillMin: 30 };
  }

  const installablePromptCount = countInstallablePrompts(manifest);
  const installableSkillCount = countInstallableSkills(manifest);
  return {
    promptMin: Math.max(1, installablePromptCount - SAFETY_BUFFER),
    skillMin: Math.max(1, installableSkillCount - SAFETY_BUFFER),
  };
}