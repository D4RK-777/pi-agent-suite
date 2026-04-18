arsed.missionDir, 'missions/demo');
    assert.deepEqual(runParsed.codexArgs, ['--model', 'gpt-5']);

    const bareParsed = parseAutoresearchArgs(['missions/demo', '--model', 'gpt-5']);
    assert.equal(bareParsed.runSubcommand, undefined);
    assert.equal(bareParsed.missionDir, 'missions/demo');
    assert.deepEqual(bareParsed.codexArgs, ['--model', 'gpt-5']);
  });


  it('resolves guided deep-interview artifacts by seeded slug even when file mtimes predate launch timestamp', async () => {
    const repo = await initRepo();
    const fakeBin = await mkdtemp(join(tmpdir(), 'omx-autoresearch-deep-interview-mtime-bin-'));
    try {
      const fakeCodexPath = join(fakeBin, 'codex');
      await writeFile(
        fakeCodexPath,
        `#!/bin/sh
if [ "$1" = "exec" ]; then