nore' });
  execFileSync('git', ['commit', '-m', 'init'], { cwd, stdio: 'ignore' });
  return cwd;
}

describe('autoresearch contracts', () => {
  it('slugifies mission names deterministically', () => {
    assert.equal(slugifyMissionName('Missions/My Demo Mission'), 'missions-my-demo-mission');
  });

  it('parses sandbox contract with evaluator command and json format', () => {
    const parsed = parseSandboxContract(`---\nevaluator:\n  command: node scripts/eval.js\n  format: json\n---\nStay in bounds.\n`);
    assert.equal(parsed.evaluator.command, 'node scripts/eval.js');
    assert.equal(parsed.evaluator.format, 'json');
    assert.equal(parsed.body, 'Stay in bounds.');
  });