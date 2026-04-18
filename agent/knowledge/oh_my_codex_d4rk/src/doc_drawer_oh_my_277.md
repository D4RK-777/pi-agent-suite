templatePath = join(pkgRoot, "templates", "AGENTS.md");
  return readFile(templatePath, "utf-8");
}

export async function renderManagedProjectRootAgents(
  existingContent?: string,
): Promise<string> {
  const template = applyProjectScopePathRewritesToAgentsTemplate(
    await readProjectRootTemplate(),
  );
  const manual = extractManualSection(
    existingContent,
    `## Local Notes\n- Add repo-specific architecture notes, workflow conventions, and verification commands here.\n- This block is preserved by \`omx agents-init\` refreshes.`,
  );
  return wrapManagedContent(template, manual);
}