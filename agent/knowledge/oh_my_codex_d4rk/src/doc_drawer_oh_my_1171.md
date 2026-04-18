execFileSync('git', ['commit', '-m', 'add autoresearch mission'], { cwd: repo, stdio: 'ignore' });

      const fakeCodexPath = join(fakeBin, 'codex');
      await writeFile(
        fakeCodexPath,
        `#!/bin/sh
candidate_file=$(find "$OMX_TEST_REPO_ROOT/.omx/logs/autoresearch" -name candidate.json | head -n 1)
head_commit=$(git rev-parse HEAD)
cat >"$candidate_file" <<'EOF'
{
  "status": "abort",
  "candidate_commit": null,
  "base_commit": "HEAD_PLACEHOLDER",
  "description": "stop after foreground fallback",
  "notes": ["fake codex exec"],
  "created_at": "2026-03-18T00:00:00.000Z"
}
EOF
perl -0pi -e "s/HEAD_PLACEHOLDER/$head_commit/g" "$candidate_file"
`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });