readFile(src, "utf-8"),
    readFile(dst, "utf-8"),
  ]);
  return srcContent !== dstContent;
}

function containsTomlKey(content: string, key: string): boolean {
  const escapedKey = key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  return new RegExp(`^\\s*${escapedKey}\\s*=`, "m").test(content);
}

function parseSkillFrontmatterScalar(
  value: string,
  key: string,
  filePath: string,
): string {
  const trimmed = value.trim();
  if (!trimmed) {
    throw new Error(`${filePath} frontmatter "${key}" must not be empty`);
  }
  if (trimmed === "|" || trimmed === ">") {
    throw new Error(
      `${filePath} frontmatter "${key}" must be a single-line string`,
    );
  }