+ eol;
  }

  const lines = content.split(/\r?\n/);
  let replaced = false;
  let inTopLevel = true;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    if (/^\[[^[\]]+\]\s*(#.*)?$/.test(trimmed)) {
      inTopLevel = false;
      continue;
    }
    if (!inTopLevel) continue;
    const match = line.match(/^\s*([A-Za-z0-9_.-]+)\s*=/);
    if (match && match[1] === key) {
      lines[i] = assignment;
      replaced = true;
      break;
    }
  }