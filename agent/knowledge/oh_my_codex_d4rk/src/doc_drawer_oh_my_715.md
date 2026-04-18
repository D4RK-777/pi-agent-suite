throw new Error(
      `${filePath} frontmatter "${key}" must be a single-line string`,
    );
  }

  const quote = trimmed[0];
  if (quote === '"' || quote === "'") {
    if (trimmed.length < 2 || trimmed.at(-1) !== quote) {
      throw new Error(
        `${filePath} frontmatter "${key}" has an unterminated quoted string`,
      );
    }
    const unquoted = trimmed.slice(1, -1).trim();
    if (!unquoted) {
      throw new Error(`${filePath} frontmatter "${key}" must not be empty`);
    }
    return unquoted;
  }

  const unquoted = trimmed.replace(/\s+#.*$/, "").trim();
  if (!unquoted) {
    throw new Error(`${filePath} frontmatter "${key}" must not be empty`);
  }
  return unquoted;
}