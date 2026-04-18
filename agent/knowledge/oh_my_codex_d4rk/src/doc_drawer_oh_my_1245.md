routing/,
      );
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('warns when canonical and legacy skill roots overlap', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-skill-overlap-'));
    try {
      const home = join(wd, 'home');
      const codexDir = join(home, '.codex');
      const canonicalHelp = join(codexDir, 'skills', 'help');
      const canonicalPlan = join(codexDir, 'skills', 'plan');
      const legacyHelp = join(home, '.agents', 'skills', 'help');
      await mkdir(canonicalHelp, { recursive: true });
      await mkdir(canonicalPlan, { recursive: true });
      await mkdir(legacyHelp, { recursive: true });
      await writeFile(join(canonicalHelp, 'SKILL.md'), '# canonical help\n');