esearchArgs(['init']);
    assert.equal(bare.guided, true);
    assert.deepEqual(bare.initArgs, []);

    const flagged = parseAutoresearchArgs(['init', '--topic', 'Ship feature']);
    assert.equal(flagged.guided, true);
    assert.deepEqual(flagged.initArgs, ['--topic', 'Ship feature']);
  });

  it('parses explicit run subcommand without breaking bare mission-dir execution', () => {
    const runParsed = parseAutoresearchArgs(['run', 'missions/demo', '--model', 'gpt-5']);
    assert.equal(runParsed.runSubcommand, true);
    assert.equal(runParsed.missionDir, 'missions/demo');
    assert.deepEqual(runParsed.codexArgs, ['--model', 'gpt-5']);