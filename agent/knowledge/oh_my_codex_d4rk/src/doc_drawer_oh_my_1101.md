ROOT_DEFAULT_OK/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('supports claude --print and gemini --prompt end-to-end through omx ask', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-ask-provider-flags-'));
    try {
      const fakeBin = join(wd, 'bin');
      await mkdir(fakeBin, { recursive: true });

      await writeFile(
        join(fakeBin, 'claude'),
        '#!/bin/sh\nif [ \"$1\" = \"--version\" ]; then echo \"fake-claude\"; exit 0; fi\nif [ \"$1\" = \"-p\" ]; then echo \"CLAUDE_PRINT_OK:$2\"; exit 0; fi\necho \"unexpected\" 1>&2\nexit 3\n',
      );
      await chmod(join(fakeBin, 'claude'), 0o755);