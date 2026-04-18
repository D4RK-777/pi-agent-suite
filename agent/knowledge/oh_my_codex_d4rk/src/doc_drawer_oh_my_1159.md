{repo}"
  },
  "draftArtifactPath": "${repo}/.omx/specs/deep-interview-autoresearch-test-launch.md",
  "missionArtifactPath": "${repo}/.omx/specs/autoresearch-test-launch/mission.md",
  "sandboxArtifactPath": "${repo}/.omx/specs/autoresearch-test-launch/sandbox.md",
  "launchReady": true,
  "blockedReasons": []
}
EOF
`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });