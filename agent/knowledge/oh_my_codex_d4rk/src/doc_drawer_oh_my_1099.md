e-override-ok\n');
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('uses package-root advisor script path from non-package cwd and still writes artifact', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-ask-nonroot-'));
    try {
      const fakeBin = join(wd, 'bin');
      await mkdir(fakeBin, { recursive: true });
      await writeFile(
        join(fakeBin, 'claude'),
        '#!/bin/sh\nif [ "$1" = "--version" ]; then echo "fake-claude"; exit 0; fi\nif [ "$1" = "-p" ]; then echo "NONROOT_DEFAULT_OK"; exit 0; fi\necho "unexpected" 1>&2\nexit 3\n',
      );
      await chmod(join(fakeBin, 'claude'), 0o755);