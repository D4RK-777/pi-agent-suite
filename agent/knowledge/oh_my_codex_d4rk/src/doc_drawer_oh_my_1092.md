urn { status: r.status, stdout: r.stdout || '', stderr: r.stderr || '', error: r.error?.message };
}

function shouldSkipForSpawnPermissions(err?: string): boolean {
  return typeof err === 'string' && /(EPERM|EACCES)/i.test(err);
}

describe('parseAskArgs', () => {
  it('parses positional prompt form', () => {
    assert.deepEqual(parseAskArgs(['claude', 'review', 'this']), {
      provider: 'claude',
      prompt: 'review this',
    });
  });

  it('parses -p prompt form', () => {
    assert.deepEqual(parseAskArgs(['gemini', '-p', 'brainstorm', 'ideas']), {
      provider: 'gemini',
      prompt: 'brainstorm ideas',
    });
  });