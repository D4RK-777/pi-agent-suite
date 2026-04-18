fi\necho \"unexpected\" 1>&2\nexit 3\n',
      );
      await chmod(join(fakeBin, 'claude'), 0o755);

      await writeFile(
        join(fakeBin, 'gemini'),
        '#!/bin/sh\nif [ \"$1\" = \"--version\" ]; then echo \"fake-gemini\"; exit 0; fi\nif [ \"$1\" = \"-p\" ]; then echo \"GEMINI_PROMPT_OK:$2\"; exit 0; fi\necho \"unexpected\" 1>&2\nexit 4\n',
      );
      await chmod(join(fakeBin, 'gemini'), 0o755);

      const env = {
        PATH: `${fakeBin}:${process.env.PATH || ''}`,
      };