{repo}"
  },
  "draftArtifactPath": "${repo}/.omx/specs/deep-interview-autoresearch-test-launch.md",
  "missionArtifactPath": "${repo}/.omx/specs/autoresearch-test-launch/mission.md",
  "sandboxArtifactPath": "${repo}/.omx/specs/autoresearch-test-launch/sandbox.md",
  "launchReady": true,
  "blockedReasons": []
}
EOF
touch -t 202603180000 "$OMX_TEST_REPO_ROOT/.omx/specs/deep-interview-autoresearch-test-launch.md"
touch -t 202603180000 "$OMX_TEST_REPO_ROOT/.omx/specs/autoresearch-test-launch/mission.md"
touch -t 202603180000 "$OMX_TEST_REPO_ROOT/.omx/specs/autoresearch-test-launch/sandbox.md"
touch -t 202603180000 "$OMX_TEST_REPO_ROOT/.omx/specs/autoresearch-test-launch/result.json"
`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });