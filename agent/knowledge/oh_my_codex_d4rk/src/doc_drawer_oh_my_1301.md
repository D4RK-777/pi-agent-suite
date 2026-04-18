ned);
    assert.equal(resolveExploreSparkShellRoute('find /tmp -maxdepth 1'), undefined);
  });
});

describe('exploreCommand', () => {
  it('routes qualifying read-only shell commands through sparkshell instead of the direct harness', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-explore-sparkshell-route-'));
    try {
      const sparkshellStub = join(wd, 'sparkshell-stub.sh');
      const harnessStub = join(wd, 'explore-stub.sh');
      const capturePath = join(wd, 'sparkshell-capture.txt');
      await writeFile(
        sparkshellStub,
        `#!/bin/sh\nprintf '%s\n' "$@" > ${JSON.stringify(capturePath)}\nprintf '# Answer\n- routed via sparkshell\n'\n`,
      );
      await writeFile(harnessStub, '#!/bin/sh\nprintf harness-should-not-run\n');