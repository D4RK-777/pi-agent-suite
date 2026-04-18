aths.push(path);
      },
      now: () => now,
      writeLine: (line) => lines.push(line),
    });

    assert.equal(removedCount, 2);
    assert.deepEqual(removedPaths, ['/tmp/omc-stale-b', '/tmp/omx-stale-a']);
    assert.match(lines.join('\n'), /Removed stale \/tmp directory: \/tmp\/omc-stale-b/);
    assert.match(lines.join('\n'), /Removed stale \/tmp directory: \/tmp\/omx-stale-a/);
    assert.match(lines.join('\n'), /Removed 2 stale OMX \/tmp directories\./);
  });
});

describe('cleanupCommand', () => {
  it('runs tmp cleanup after orphaned MCP cleanup', async () => {
    const calls: string[] = [];