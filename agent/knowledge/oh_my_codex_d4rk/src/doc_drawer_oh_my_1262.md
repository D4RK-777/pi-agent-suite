n.json')), false);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('passes exec --help through to codex exec', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-exec-help-'));
    try {
      const home = join(wd, 'home');
      const fakeBin = join(wd, 'bin');
      const fakeCodexPath = join(fakeBin, 'codex');

      await mkdir(home, { recursive: true });
      await mkdir(fakeBin, { recursive: true });
      await writeFile(fakeCodexPath, '#!/bin/sh\nprintf \'fake-codex:%s\\n\' \"$*\"\n');
      await chmod(fakeCodexPath, 0o755);