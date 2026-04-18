'home');
      const fakeBin = join(wd, 'bin');
      const fakeCodexPath = join(fakeBin, 'codex');

      await mkdir(join(home, '.codex'), { recursive: true });
      await mkdir(fakeBin, { recursive: true });
      await writeFile(join(home, '.codex', 'AGENTS.md'), '# User Instructions\n\nGlobal guidance.\n');
      await writeFile(join(wd, 'AGENTS.md'), '# Project Instructions\n\nProject guidance.\n');
      await writeFile(
        fakeCodexPath,
        [
          '#!/bin/sh',
          'printf \'fake-codex:%s\\n\' "$*"',
          'for arg in "$@"; do',
          '  case "$arg" in',
          '    model_instructions_file=*)',
          '      file=$(printf %s "$arg" | sed \'s/^model_instructions_file="//; s/"$//\')',
          '      printf \'instructions-path:%s\\n\' "$file"',