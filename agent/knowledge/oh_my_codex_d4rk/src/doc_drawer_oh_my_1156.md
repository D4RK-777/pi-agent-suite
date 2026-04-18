EPO_ROOT/.omx/logs/autoresearch" -name candidate.json | head -n 1)
head_commit=$(git rev-parse HEAD)
cat >"$candidate_file" <<'EOF'
{
  "status": "abort",
  "candidate_commit": null,
  "base_commit": "HEAD_PLACEHOLDER",
  "description": "stop after guided handoff",
  "notes": ["fake codex exec"],
  "created_at": "2026-03-18T00:00:00.000Z"
}
EOF
perl -0pi -e "s/HEAD_PLACEHOLDER/$head_commit/g" "$candidate_file"
exit 0
fi
mkdir -p "$OMX_TEST_REPO_ROOT/.omx/specs/deep-int"
mkdir -p "$OMX_TEST_REPO_ROOT/.omx/specs/autoresearch-test-launch"
cat >"$OMX_TEST_REPO_ROOT/.omx/specs/deep-interview-autoresearch-test-launch.md" <<'EOF'
# Deep Interview Autoresearch Draft — test-launch

## Mission Draft
Investigate flaky onboarding behavior

## Evaluator Draft
node scripts/eval.js