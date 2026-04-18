atcher pid file/);
    assert.match(source, /failed to remove hook-derived watcher pid file/);
  });

  it('replaces silent log-write catches with warning logs', async () => {
    const loggingSource = await readSource('src/hooks/extensibility/logging.ts');
    const dispatchSource = await readSource('src/hooks/extensibility/dispatcher.ts');
    const keywordSource = await readSource('src/hooks/keyword-detector.ts');

    assert.ok(!loggingSource.includes('.catch(() => {});'));
    assert.ok(!dispatchSource.includes('.catch(() => {});'));
    assert.ok(!keywordSource.includes('.catch(() => {});'));