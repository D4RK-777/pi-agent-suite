force" once\)/,
      );
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('warns when explore harness sources are packaged but cargo is unavailable', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-explore-copy-'));
    try {
      await withPackagedExploreHarnessHidden(async () => {
        const home = join(wd, 'home');
        const codexDir = join(home, '.codex');
        const fakeBin = join(wd, 'bin');
        await mkdir(codexDir, { recursive: true });
        await mkdir(fakeBin, { recursive: true });
        await writeFile(join(fakeBin, 'codex'), '#!/bin/sh\necho "codex test"\n');
        spawnSync('chmod', ['+x', join(fakeBin, 'codex')], { encoding: 'utf-8' });