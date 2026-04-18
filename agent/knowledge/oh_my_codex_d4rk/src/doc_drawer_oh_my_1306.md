ered the lookup/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('falls back to the explore harness when sparkshell is GLIBC-incompatible', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-explore-sparkshell-glibc-'));
    try {
      const sparkshellStub = join(wd, 'sparkshell-stub.sh');
      const harnessStub = join(wd, 'explore-stub.sh');
      await writeFile(
        sparkshellStub,
        "#!/bin/sh\necho \"omx-sparkshell: /lib/x86_64-linux-gnu/libc.so.6: version \\`GLIBC_2.39' not found\" 1>&2\nexit 1\n",
      );
      await writeFile(
        harnessStub,
        '#!/bin/sh\nprintf "%s\\n" "# Answer" "- fallback harness recovered the lookup"\n',
      );
      await chmod(sparkshellStub, 0o755);