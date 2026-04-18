\t/g, '  ');
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    const sectionMatch = /^([A-Za-z0-9_-]+):\s*$/.exec(trimmed);
    if (sectionMatch) {
      currentSection = sectionMatch[1];
      result[currentSection] = {};
      continue;
    }

    const nestedMatch = /^([A-Za-z0-9_-]+):\s*(.+)\s*$/.exec(trimmed);
    if (!nestedMatch) {
      throw contractError(`Unsupported sandbox.md frontmatter line: ${trimmed}`);
    }