EPO_ROOT/.omx/logs/autoresearch" -name candidate.json | head -n 1)
head_commit=$(git rev-parse HEAD)
printf '{\\n  "status": "abort",\\n  "candidate_commit": null,\\n  "base_commit": "%s",\\n  "description": "stop after first exec",\\n  "notes": ["fake codex exec"],\\n  "created_at": "2026-03-15T00:00:00.000Z"\\n}\\n' "$head_commit" >"$candidate_file"
`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });

      const result = runOmx(
        repo,
        ['autoresearch', missionDir, '--dangerously-bypass-approvals-and-sandbox'],
        { PATH: `${fakeBin}:${process.env.PATH || ''}`, OMX_TEST_REPO_ROOT: repo },
      );