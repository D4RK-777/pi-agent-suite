aths.push(path);
      },
      now: () => now,
      writeLine: (line) => lines.push(line),
    });

    assert.equal(removedCount, 0);
    assert.deepEqual(removedPaths, []);
    assert.match(
      lines.join('\n'),
      /Dry run: would remove 2 stale OMX \/tmp directories:/,
    );
    assert.match(lines.join('\n'), /\/tmp\/omc-stale-b/);
    assert.match(lines.join('\n'), /\/tmp\/omx-stale-a/);
    assert.doesNotMatch(lines.join('\n'), /oh-my-codex-fresh/);
    assert.doesNotMatch(lines.join('\n'), /other-stale/);
  });

  it('removes only stale matching directories and returns the removed count', async () => {
    const lines: string[] = [];
    const removedPaths: string[] = [];
    const now = 10 * 60 * 60 * 1000;