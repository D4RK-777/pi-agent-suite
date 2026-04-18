promptsDir, 'executor.md'),
        'You are Executor.\nFollow strict verification rules.',
      );

      await writeFile(
        join(fakeBin, 'claude'),
        '#!/bin/sh\nif [ \"$1\" = \"--version\" ]; then echo \"fake-claude\"; exit 0; fi\nif [ \"$1\" = \"-p\" ]; then echo \"CLAUDE_FINAL_PROMPT:$2\"; exit 0; fi\necho \"unexpected\" 1>&2\nexit 3\n',
      );
      await chmod(join(fakeBin, 'claude'), 0o755);

      const res = runOmx(
        wd,
        ['ask', 'claude', '--agent-prompt', 'executor', 'ship', 'feature'],
        { PATH: `${fakeBin}:${process.env.PATH || ''}`, CODEX_HOME: codexHome },
      );
      if (shouldSkipForSpawnPermissions(res.error)) return;