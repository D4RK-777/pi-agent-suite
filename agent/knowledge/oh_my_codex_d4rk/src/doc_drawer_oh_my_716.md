throw new Error(`${filePath} frontmatter "${key}" must not be empty`);
  }
  return unquoted;
}

export function parseSkillFrontmatter(
  content: string,
  filePath = "SKILL.md",
): SkillFrontmatterMetadata {
  const frontmatterMatch = content.match(
    /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/,
  );
  if (!frontmatterMatch) {
    throw new Error(
      `${filePath} must start with YAML frontmatter containing non-empty name and description fields`,
    );
  }

  let name: string | undefined;
  let description: string | undefined;
  const lines = frontmatterMatch[1].split(/\r?\n/);