sage}; Codex Enable/Disable Skills may show duplicates until ~/.agents/skills is cleaned up`,
  };
}

async function checkSkills(dir: string): Promise<Check> {
  const expectations = getCatalogExpectations();
  if (!existsSync(dir)) {
    return { name: 'Skills', status: 'warn', message: 'skills directory not found' };
  }
  try {
    const entries = await readdir(dir, { withFileTypes: true });
    const skillDirs = entries.filter(e => e.isDirectory());
    if (skillDirs.length >= expectations.skillMin) {
      return { name: 'Skills', status: 'pass', message: `${skillDirs.length} skills installed` };
    }
    return { name: 'Skills', status: 'warn', message: `${skillDirs.length} skills (expected >= ${expectations.skillMin})` };
  } catch {