);
      });
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('passes explore harness check when a packaged native binary is present even without cargo', async () => {
    await withPackagedExploreHarnessLock(async () => {
      const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-explore-binary-'));
      try {
        const home = join(wd, 'home');
        const codexDir = join(home, '.codex');
        const fakeBin = join(wd, 'bin');
        const packageBinDir = join(process.cwd(), 'bin');
        const packagedBinary = join(packageBinDir, process.platform === 'win32' ? 'omx-explore-harness.exe' : 'omx-explore-harness');
        const packagedMeta = join(packageBinDir, 'omx-explore-harness.meta.json');