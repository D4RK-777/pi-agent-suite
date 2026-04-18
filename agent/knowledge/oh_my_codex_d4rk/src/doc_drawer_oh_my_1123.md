parseInitArgs(['--unknown-flag', 'value']),
      /Unknown init flag: --unknown-flag/,
    );
  });

  it('sanitizes slug via slugifyMissionName', () => {
    const result = parseInitArgs(['--slug', '../../etc/cron.d/omx']);
    assert.ok(result.slug);
    assert.doesNotMatch(result.slug!, /\.\./);
    assert.doesNotMatch(result.slug!, /\//);
  });
});

describe('checkTmuxAvailable', () => {
  it('returns a boolean', () => {
    const result = checkTmuxAvailable();
    assert.equal(typeof result, 'boolean');
  });
});