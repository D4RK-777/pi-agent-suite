hSource.includes('.catch(() => {});'));
    assert.ok(!keywordSource.includes('.catch(() => {});'));

    assert.match(loggingSource, /failed to append hook plugin log entry/);
    assert.match(dispatchSource, /failed to append hook dispatch log entry/);
    assert.match(keywordSource, /failed to persist keyword activation state/);
  });
});