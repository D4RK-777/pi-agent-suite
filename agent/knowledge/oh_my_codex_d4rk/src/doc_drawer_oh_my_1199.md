keNow += ms;
      },
      now: () => fakeNow,
      writeLine: (line) => lines.push(line),
    });

    assert.equal(result.terminatedCount, 2);
    assert.equal(result.forceKilledCount, 1);
    assert.deepEqual(result.failedPids, []);
    assert.deepEqual(signals, [
      { pid: 800, signal: 'SIGTERM' },
      { pid: 810, signal: 'SIGTERM' },
      { pid: 810, signal: 'SIGKILL' },
    ]);
    assert.match(lines.join('\n'), /Escalating to SIGKILL for 1 process/);
    assert.match(lines.join('\n'), /Killed 2 orphaned OMX MCP server process\(es\) \(1 required SIGKILL\)\./);
  });
});