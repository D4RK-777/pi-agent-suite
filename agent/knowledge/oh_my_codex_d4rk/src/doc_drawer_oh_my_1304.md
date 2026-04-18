g', '--oneline']);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('falls back to the explore harness when sparkshell backend is unavailable', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-explore-sparkshell-fallback-'));
    try {
      const harnessStub = join(wd, 'explore-stub.sh');
      await writeFile(
        harnessStub,
        '#!/bin/sh\nprintf "%s\\n" "# Answer" "- fallback harness recovered the lookup"\n',
      );
      await chmod(harnessStub, 0o755);

      const result = runOmx(wd, ['explore', '--prompt', 'git log --oneline'], {
        OMX_SPARKSHELL_BIN: join(wd, 'missing-sparkshell'),
        OMX_EXPLORE_BIN: harnessStub,
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;