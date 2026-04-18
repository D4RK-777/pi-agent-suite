emini-long-flag/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('injects --agent-prompt content into final prompt while keeping Original task raw', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-ask-agent-prompt-'));
    try {
      const fakeBin = join(wd, 'bin');
      const codexHome = join(wd, '.codex-home');
      const promptsDir = join(codexHome, 'prompts');
      await mkdir(fakeBin, { recursive: true });
      await mkdir(promptsDir, { recursive: true });

      await writeFile(
        join(promptsDir, 'executor.md'),
        'You are Executor.\nFollow strict verification rules.',
      );