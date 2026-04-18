nal: () => {
        signalCount += 1;
      },
      writeLine: (line) => lines.push(line),
    });

    assert.equal(result.dryRun, true);
    assert.equal(result.candidates.length, 3);
    assert.equal(signalCount, 0);
    assert.match(lines.join('\n'), /Dry run: would terminate 3 orphaned OMX MCP server process/);
    assert.match(lines.join('\n'), /PID 800/);
    assert.match(lines.join('\n'), /PID 810/);
  });

  it('sends SIGTERM, waits, and escalates with SIGKILL when needed', async () => {
    const lines: string[] = [];
    const signals: Array<{ pid: number; signal: NodeJS.Signals }> = [];
    const alive = new Set([800, 810]);
    let fakeNow = 0;