execFileSync('git', ['commit', '-m', 'add autoresearch mission'], { cwd: repo, stdio: 'ignore' });

      const fakeCatPath = join(fakeBin, 'cat');
      await writeFile(
        fakeCatPath,
        `#!/bin/sh
printf 'unexpected cat invocation\\n' >&2
exit 97
`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCatPath], { stdio: 'ignore' });

      const fakeCodexPath = join(fakeBin, 'codex');
      await writeFile(
        fakeCodexPath,
        `#!/bin/sh
printf 'fake-codex:%s\\n' "$*" >&2
while IFS= read -r _; do
  :
done
candidate_file=$(find "$OMX_TEST_REPO_ROOT/.omx/logs/autoresearch" -name candidate.json | head -n 1)
head_commit=$(git rev-parse HEAD)