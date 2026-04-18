S.ProcessEnv);
    assert.deepEqual(resolved, { command: '/tmp/omx-explore-stub', args: [] });
  });

  it('prefers a packaged native harness binary when present', async () => {
    await withPackagedExploreHarnessLock(async () => {
      const wd = await mkdtemp(join(tmpdir(), 'omx-explore-native-'));
      try {
        const binDir = join(wd, 'bin');
        await mkdir(binDir, { recursive: true });
        await writeFile(join(wd, 'package.json'), '{}\n');
        await writeFile(join(binDir, 'omx-explore-harness.meta.json'), JSON.stringify({
          binaryName: packagedExploreHarnessBinaryName(),
          platform: process.platform,
          arch: process.arch,
        }));
        const nativePath = join(binDir, packagedExploreHarnessBinaryName());