tf 'missing -m model\n' >&2
  exit 1
fi
${body}
`,
  );
  await chmod(stub, 0o755);
  return stub;
}

async function writeExploreHarnessScenarioStub(wd: string, body: string): Promise<string> {
  const stub = join(wd, 'explore-scenario-stub.sh');
  await writeFile(
    stub,
    `#!/bin/sh
set -eu
${body}
`,
  );
  await chmod(stub, 0o755);
  return stub;
}

describe('parseExploreArgs', () => {
  it('parses --prompt form', () => {
    assert.deepEqual(parseExploreArgs(['--prompt', 'find', 'auth']), { prompt: 'find auth' });
  });

  it('parses --prompt= form', () => {
    assert.deepEqual(parseExploreArgs(['--prompt=find auth']), { prompt: 'find auth' });
  });