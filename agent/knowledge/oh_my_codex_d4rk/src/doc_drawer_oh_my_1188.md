cFileSync('git', ['commit', '-m', 'add autoresearch noop mission'], { cwd: repo, stdio: 'ignore' });

      const fakeCodexPath = join(fakeBin, 'codex');
      await writeFile(
        fakeCodexPath,
        `#!/bin/sh
cat >/dev/null
candidate_file=$(find "$OMX_TEST_REPO_ROOT/.omx/logs/autoresearch" -name candidate.json | head -n 1)
head_commit=$(git rev-parse HEAD)
cat >"$candidate_file" <<EOF
{
  "status": "noop",
  "candidate_commit": null,
  "base_commit": "$head_commit",
  "description": "noop from fake codex exec",
  "notes": ["fake noop"],
  "created_at": "2026-03-15T00:00:00.000Z"
}
EOF
`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });