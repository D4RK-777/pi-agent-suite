ndefined;
  let description: string | undefined;
  const lines = frontmatterMatch[1].split(/\r?\n/);

  for (const [index, rawLine] of lines.entries()) {
    const line = rawLine.trimEnd();
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    if (/^\s/.test(rawLine)) continue;

    const match = line.match(/^([A-Za-z0-9_-]+):(.*)$/);
    if (!match) {
      throw new Error(
        `${filePath} has invalid YAML frontmatter on line ${index + 2}: ${trimmed}`,
      );
    }

    const [, key, rawValue] = match;
    if (!rawValue.trim()) continue;

    const parsedValue = parseSkillFrontmatterScalar(rawValue, key, filePath);
    if (key === "name") name = parsedValue;
    if (key === "description") description = parsedValue;
  }