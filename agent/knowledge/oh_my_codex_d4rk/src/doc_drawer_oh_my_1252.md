e }).catch(() => {});"));
    assert.ok(!source.includes('await unlink(pidPath).catch(() => {});'));

    const esrchGuardCount =
      source.match(/if \(!hasErrnoCode\(error, ['"]ESRCH['"]\)\)/g)?.length ?? 0;
    assert.equal(esrchGuardCount, 2);
    assert.match(source, /failed to write notify fallback watcher pid file/);
    assert.match(source, /failed to write hook-derived watcher pid file/);
    assert.match(source, /failed to remove notify fallback watcher pid file/);
    assert.match(source, /failed to remove hook-derived watcher pid file/);
  });