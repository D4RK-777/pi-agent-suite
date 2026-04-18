ative(dir, parentAgentsPath).replaceAll("\\", "/");
  return `<!-- Parent: ${relativePath} -->\n`;
}

export async function renderManagedDirectoryAgents(
  dir: string,
  existingContent?: string,
  assumeParentAgents = false,
): Promise<string> {
  const snapshot = await snapshotDirectory(dir);
  const manual = extractManualSection(
    existingContent,
    `## Local Notes\n- Add subtree-specific constraints, ownership notes, and test commands here.\n- Keep notes scoped to this directory and its children.`,
  );
  const title = basename(dir);
  const relativeDir = relative(process.cwd(), dir).replaceAll("\\", "/") || ".";
  const parentReference = renderParentReference(dir, assumeParentAgents);