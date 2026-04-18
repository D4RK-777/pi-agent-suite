aleCompare(b));
  directories.sort((a, b) => a.localeCompare(b));
  return { files, directories };
}

function renderParentReference(
  dir: string,
  assumeParentAgents = false,
): string {
  const parentAgentsPath = join(dirname(dir), "AGENTS.md");
  if (!assumeParentAgents && !existsSync(parentAgentsPath)) return "";
  const relativePath = relative(dir, parentAgentsPath).replaceAll("\\", "/");
  return `<!-- Parent: ${relativePath} -->\n`;
}