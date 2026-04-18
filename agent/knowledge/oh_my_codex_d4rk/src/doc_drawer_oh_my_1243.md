], { encoding: 'utf-8' });
          } else {
            await rm(packagedBinary, { force: true });
          }
          if (originalMeta !== null) {
            await writeFile(packagedMeta, originalMeta);
          } else {
            await rm(packagedMeta, { force: true });
          }
        }
      } finally {
        await rm(wd, { recursive: true, force: true });
      }
    });
  });

  it('warns when explore routing is explicitly disabled in config.toml', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-explore-routing-'));
    try {
      const home = join(wd, 'home');
      const codexDir = join(home, '.codex');
      await mkdir(codexDir, { recursive: true });
      await writeFile(
        join(codexDir, 'config.toml'),
        `
[env]