preserved by \`omx agents-init\` refreshes.`,
  );
  return wrapManagedContent(template, manual);
}

function formatList(
  items: string[],
  suffix = "",
  limit = DEFAULT_LIST_LIMIT,
): string[] {
  if (items.length === 0) return ["- None"];
  const visible = items.slice(0, limit).map((item) => `- \`${item}${suffix}\``);
  if (items.length > limit) {
    visible.push(`- ...and ${items.length - limit} more`);
  }
  return visible;
}

async function snapshotDirectory(dir: string): Promise<DirectorySnapshot> {
  const entries = await readdir(dir, { withFileTypes: true });
  const files: string[] = [];
  const directories: string[] = [];