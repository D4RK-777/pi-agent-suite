rt = "medium"$/m);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('edits an existing agent via $EDITOR and removes it with --force', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-cli-'));
    const home = join(wd, 'home');
    try {
      const projectAgentsDir = join(wd, '.codex', 'agents');
      await mkdir(projectAgentsDir, { recursive: true });
      await mkdir(home, { recursive: true });
      const agentPath = join(projectAgentsDir, 'editor-test.toml');
      await writeFile(
        agentPath,
        'name = "editor-test"\ndescription = "Before edit"\ndeveloper_instructions = """before"""\n',
      );