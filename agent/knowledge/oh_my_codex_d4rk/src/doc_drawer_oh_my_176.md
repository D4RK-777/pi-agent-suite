description: 'candidate',
      notes: [],
      created_at: '2026-03-14T05:00:00.000Z',
    };

    const ambiguous = decideAutoresearchOutcome(
      { keep_policy: 'score_improvement', last_kept_score: null },
      candidate,
      { command: 'node eval.js', ran_at: '2026-03-14T05:00:01.000Z', status: 'pass', pass: true, exit_code: 0 },
    );
    assert.equal(ambiguous.decision, 'ambiguous');
    assert.equal(ambiguous.keep, false);

    const kept = decideAutoresearchOutcome(
      { keep_policy: 'pass_only', last_kept_score: null },
      candidate,
      { command: 'node eval.js', ran_at: '2026-03-14T05:00:01.000Z', status: 'pass', pass: true, exit_code: 0 },
    );
    assert.equal(kept.decision, 'keep');
    assert.equal(kept.keep, true);
  });