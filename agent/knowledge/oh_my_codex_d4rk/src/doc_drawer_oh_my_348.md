arch(/^##\s+/m);
  return (nextHeading >= 0 ? remainder.slice(0, nextHeading) : remainder).trim();
}

function parseLaunchReadinessSection(section: string): { launchReady: boolean; blockedReasons: string[] } {
  const normalized = section.trim();
  if (!normalized) {
    return { launchReady: false, blockedReasons: ['Launch readiness section is missing.'] };
  }

  const launchReady = /Launch-ready:\s*yes/i.test(normalized);
  const blockedReasons = launchReady
    ? []
    : normalized
      .split(/\r?\n/)
      .map((line) => line.trim())
      .filter((line) => /^-\s+/.test(line))
      .map((line) => line.replace(/^-\s+/, '').trim())
      .filter(Boolean);

  return { launchReady, blockedReasons };
}