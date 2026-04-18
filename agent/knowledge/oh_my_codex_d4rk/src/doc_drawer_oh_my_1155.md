ursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });

  it('launches interactive deep-interview intake, materializes mission files, and then prefers split-pane handoff', async () => {
    const repo = await initRepo();
    const fakeBin = await mkdtemp(join(tmpdir(), 'omx-autoresearch-deep-interview-bin-'));
    try {
      const codexLog = join(repo, 'codex-launch.log');
      const tmuxLog = join(repo, 'guided-tmux.log');
      const fakeCodexPath = join(fakeBin, 'codex');
      await writeFile(
        fakeCodexPath,
        `#!/bin/sh
printf '%s\n' "$*" >>"${codexLog}"
if [ "$1" = "exec" ]; then
candidate_file=$(find "$OMX_TEST_REPO_ROOT/.omx/logs/autoresearch" -name candidate.json | head -n 1)
head_commit=$(git rev-parse HEAD)