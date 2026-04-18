<mission-dir>/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }
  });

  it('treats top-level topic/evaluator flags as seeded deep-interview input', () => {
    const parsed = parseAutoresearchArgs(['--topic', 'Improve docs', '--evaluator', 'node eval.js', '--slug', 'docs-run']);
    assert.equal(parsed.guided, true);
    assert.equal(parsed.seedArgs?.topic, 'Improve docs');
    assert.equal(parsed.seedArgs?.evaluatorCommand, 'node eval.js');
    assert.equal(parsed.seedArgs?.slug, 'docs-run');
  });

  it('treats bare init as guided alias and init with flags as expert init args', () => {
    const bare = parseAutoresearchArgs(['init']);
    assert.equal(bare.guided, true);
    assert.deepEqual(bare.initArgs, []);