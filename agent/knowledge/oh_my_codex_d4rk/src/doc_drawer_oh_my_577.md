match || match[1] !== key) continue;
    return parseTomlStringValue(match[2]);
  }
  return null;
}

export function upsertTopLevelTomlString(
  content: string,
  key: string,
  value: string,
): string {
  const eol = content.includes("\r\n") ? "\r\n" : "\n";
  const assignment = `${key} = "${escapeTomlString(value)}"`;

  if (!content.trim()) {
    return assignment + eol;
  }

  const lines = content.split(/\r?\n/);
  let replaced = false;
  let inTopLevel = true;