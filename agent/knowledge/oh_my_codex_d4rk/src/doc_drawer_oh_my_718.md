f (key === "name") name = parsedValue;
    if (key === "description") description = parsedValue;
  }

  if (!name) {
    throw new Error(`${filePath} is missing a non-empty frontmatter "name"`);
  }
  if (!description) {
    throw new Error(
      `${filePath} is missing a non-empty frontmatter "description"`,
    );
  }

  return { name, description };
}

export async function validateSkillFile(skillMdPath: string): Promise<void> {
  const content = await readFile(skillMdPath, "utf-8");
  parseSkillFrontmatter(content, skillMdPath);
}

async function buildLegacySkillOverlapNotice(
  scope: SetupScope,
): Promise<LegacySkillOverlapNotice> {
  if (scope !== "user") {
    return { shouldWarn: false, message: "" };
  }