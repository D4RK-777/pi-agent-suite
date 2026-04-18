ll\n'\n`,
      );
      await writeFile(harnessStub, '#!/bin/sh\nprintf harness-should-not-run\n');
      await chmod(sparkshellStub, 0o755);
      await chmod(harnessStub, 0o755);

      const result = runOmx(wd, ['explore', '--prompt', 'git log --oneline'], {
        OMX_SPARKSHELL_BIN: sparkshellStub,
        OMX_EXPLORE_BIN: harnessStub,
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;