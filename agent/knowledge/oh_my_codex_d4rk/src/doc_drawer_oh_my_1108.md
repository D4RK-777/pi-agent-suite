E_FINAL_PROMPT:/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('fails clearly when --agent-prompt role is missing from prompts directory', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-ask-agent-prompt-missing-'));
    try {
      const fakeBin = join(wd, 'bin');
      const codexHome = join(wd, '.codex-home');
      const promptsDir = join(codexHome, 'prompts');
      await mkdir(fakeBin, { recursive: true });
      await mkdir(promptsDir, { recursive: true });