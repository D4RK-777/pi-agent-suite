ion `GLIBC_2\.39' not found/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('passes prompt to harness and preserves markdown stdout', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-explore-cmd-'));
    try {
      const stub = join(wd, 'explore-stub.sh');
      const capturePath = join(wd, 'capture.txt');
      await writeFile(
        stub,
        `#!/bin/sh\nprintf '%s\n' \"$@\" > ${JSON.stringify(capturePath)}\nprintf '# Files\\n- demo\\n'\n`,
      );
      await chmod(stub, 0o755);