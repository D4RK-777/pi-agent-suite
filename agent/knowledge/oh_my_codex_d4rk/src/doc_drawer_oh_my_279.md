dir(dir, { withFileTypes: true });
  const files: string[] = [];
  const directories: string[] = [];

  for (const entry of entries) {
    if (entry.name === "AGENTS.md") continue;
    if (entry.isDirectory()) {
      if (IGNORE_DIRECTORY_NAMES.has(entry.name)) continue;
      directories.push(entry.name);
      continue;
    }
    if (entry.isFile()) {
      files.push(entry.name);
    }
  }

  files.sort((a, b) => a.localeCompare(b));
  directories.sort((a, b) => a.localeCompare(b));
  return { files, directories };
}