result.stdout || '',
    stderr: result.stderr || '',
    error: result.error?.message || '',
  };
}

describe('omx exec', () => {
  it('runs codex exec with session-scoped instructions that preserve AGENTS and overlay content', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-exec-cli-'));
    try {
      const home = join(wd, 'home');
      const fakeBin = join(wd, 'bin');
      const fakeCodexPath = join(fakeBin, 'codex');