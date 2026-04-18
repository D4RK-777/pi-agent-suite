await mkdir(fakeBin, { recursive: true });
      await mkdir(promptsDir, { recursive: true });

      await writeFile(
        join(fakeBin, 'gemini'),
        '#!/bin/sh\nif [ \"$1\" = \"--version\" ]; then echo \"fake-gemini\"; exit 0; fi\nif [ \"$1\" = \"-p\" ]; then echo \"should-not-run\"; exit 0; fi\necho \"unexpected\" 1>&2\nexit 4\n',
      );
      await chmod(join(fakeBin, 'gemini'), 0o755);

      const res = runOmx(
        wd,
        ['ask', 'gemini', '--agent-prompt=planner', '--prompt', 'do', 'planning'],
        { PATH: `${fakeBin}:${process.env.PATH || ''}`, CODEX_HOME: codexHome },
      );
      if (shouldSkipForSpawnPermissions(res.error)) return;