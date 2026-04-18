gentPath), false);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('fails with clear guidance when remove runs in non-interactive mode without --force', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-cli-'));
    const home = join(wd, 'home');
    try {
      const projectAgentsDir = join(wd, '.codex', 'agents');
      await mkdir(projectAgentsDir, { recursive: true });
      await mkdir(home, { recursive: true });
      const agentPath = join(projectAgentsDir, 'non-interactive.toml');
      await writeFile(
        agentPath,
        'name = "non-interactive"\ndescription = "Remove me"\ndeveloper_instructions = """noop"""\n',
      );