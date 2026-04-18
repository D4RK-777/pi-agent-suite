isable Skills may show duplicates until ~\/\.agents\/skills is cleaned up/,
      );
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('passes when legacy skill root is a link to the canonical skills directory', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-skill-link-'));
    try {
      const home = join(wd, 'home');
      const codexDir = join(home, '.codex');
      const canonicalSkillsRoot = join(codexDir, 'skills');
      const canonicalHelp = join(canonicalSkillsRoot, 'help');
      const legacyRoot = join(home, '.agents', 'skills');
      await mkdir(canonicalHelp, { recursive: true });
      await mkdir(join(home, '.agents'), { recursive: true });