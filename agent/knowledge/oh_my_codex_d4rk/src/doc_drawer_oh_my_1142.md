-dangerously-bypass-approvals-and-sandbox']), ['--dangerously-bypass-approvals-and-sandbox']);
  });

  it('normalizes --madmax to the canonical bypass flag', () => {
    assert.deepEqual(normalizeAutoresearchCodexArgs(['--madmax']), ['--dangerously-bypass-approvals-and-sandbox']);
  });
});

describe('omx autoresearch', () => {
  it('documents autoresearch in top-level help', async () => {
    const cwd = await mkdtemp(join(tmpdir(), 'omx-autoresearch-help-'));
    try {
      const result = runOmx(cwd, ['--help']);
      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stdout, /omx autoresearch\s+Launch thin-supervisor autoresearch with keep\/discard\/reset parity/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }