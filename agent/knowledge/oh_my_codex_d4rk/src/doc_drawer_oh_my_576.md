el: defaultModel,
  });
  if (normalized.length === 0) return null;
  return normalized.join(" ");
}

export function readTopLevelTomlString(
  content: string,
  key: string,
): string | null {
  let inTopLevel = true;
  const lines = content.split(/\r?\n/);
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    if (/^\[[^[\]]+\]\s*(#.*)?$/.test(trimmed)) {
      inTopLevel = false;
      continue;
    }
    if (!inTopLevel) continue;
    const match = line.match(/^\s*([A-Za-z0-9_.-]+)\s*=\s*(.*?)\s*(?:#.*)?$/);
    if (!match || match[1] !== key) continue;
    return parseTomlStringValue(match[2]);
  }
  return null;
}