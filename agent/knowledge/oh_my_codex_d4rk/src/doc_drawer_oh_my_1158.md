unch
EOF
cat >"$OMX_TEST_REPO_ROOT/.omx/specs/autoresearch-test-launch/mission.md" <<'EOF'
# Mission

Investigate flaky onboarding behavior
EOF
cat >"$OMX_TEST_REPO_ROOT/.omx/specs/autoresearch-test-launch/sandbox.md" <<'EOF'
---
evaluator:
  command: node scripts/eval.js
  format: json
  keep_policy: score_improvement
---
EOF
cat >"$OMX_TEST_REPO_ROOT/.omx/specs/autoresearch-test-launch/result.json" <<'EOF'
{
  "kind": "omx.autoresearch.deep-interview/v1",
  "compileTarget": {
    "topic": "Investigate flaky onboarding behavior",
    "evaluatorCommand": "node scripts/eval.js",
    "keepPolicy": "score_improvement",
    "slug": "test-launch",
    "repoRoot": "${repo}"
  },
  "draftArtifactPath": "${repo}/.omx/specs/deep-interview-autoresearch-test-launch.md",