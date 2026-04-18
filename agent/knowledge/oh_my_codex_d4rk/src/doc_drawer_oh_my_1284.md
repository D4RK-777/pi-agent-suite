});
      } finally {
        await rm(wd, { recursive: true, force: true });
      }
    });
  });

  it('uses an existing repo-built native harness before cargo fallback', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-explore-target-'));
    try {
      const targetDir = join(wd, 'target', 'release');
      await mkdir(targetDir, { recursive: true });
      await writeFile(join(wd, 'package.json'), '{}\n');
      await writeFile(join(targetDir, packagedExploreHarnessBinaryName()), '#!/bin/sh\nexit 0\n');
      await chmod(join(targetDir, packagedExploreHarnessBinaryName()), 0o755);
      await mkdir(join(wd, 'crates', 'omx-explore'), { recursive: true });