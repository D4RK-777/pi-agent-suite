e()), args: [] });
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('builds cargo fallback command otherwise', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-explore-fallback-'));
    try {
      const crateDir = join(wd, 'crates', 'omx-explore');
      await mkdir(crateDir, { recursive: true });
      await writeFile(join(wd, 'package.json'), '{}\n');
      await writeFile(join(crateDir, 'Cargo.toml'), '[package]\nname = "omx-explore-harness"\nversion = "0.0.0"\n');