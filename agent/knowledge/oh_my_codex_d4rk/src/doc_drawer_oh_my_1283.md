cess.arch,
        }));
        const nativePath = join(binDir, packagedExploreHarnessBinaryName());
        await writeFile(nativePath, '#!/bin/sh\necho native\n');
        await chmod(nativePath, 0o755);

        const resolved = resolveExploreHarnessCommand(wd, {} as NodeJS.ProcessEnv);
        assert.deepEqual(resolved, { command: nativePath, args: [] });
      } finally {
        await rm(wd, { recursive: true, force: true });
      }
    });
  });