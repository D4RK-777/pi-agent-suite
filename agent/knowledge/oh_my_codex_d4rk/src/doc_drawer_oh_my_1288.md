, 'Cargo.toml')));
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('hydrates a native harness for packaged installs before attempting cargo fallback', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-explore-hydrated-'));
    try {
      const assetRoot = join(wd, 'assets');
      const cacheDir = join(wd, 'cache');
      const stagingDir = join(wd, 'staging');
      await mkdir(assetRoot, { recursive: true });
      await mkdir(stagingDir, { recursive: true });
      await writeFile(join(wd, 'package.json'), JSON.stringify({
        version: '0.8.15',
        repository: { url: 'git+https://github.com/Yeachan-Heo/oh-my-codex.git' },
      }));
      await mkdir(join(wd, 'crates', 'omx-explore'), { recursive: true });