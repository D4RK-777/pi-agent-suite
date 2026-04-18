stedMatch) {
      throw contractError(`Unsupported sandbox.md frontmatter line: ${trimmed}`);
    }

    const [, key, rawValue] = nestedMatch;
    const value = rawValue.replace(/^['"]|['"]$/g, '');
    if (line.startsWith(' ') || line.startsWith('\t')) {
      if (!currentSection) {
        throw contractError(`Nested sandbox.md frontmatter key requires a parent section: ${trimmed}`);
      }
      const section = result[currentSection];
      if (!section || typeof section !== 'object' || Array.isArray(section)) {
        throw contractError(`Invalid sandbox.md frontmatter section: ${currentSection}`);
      }
      (section as Record<string, unknown>)[key] = value;
      continue;
    }

    result[key] = value;
    currentSection = null;
  }

  return result;
}