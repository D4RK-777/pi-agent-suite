Id);
    await runAutoresearchLoop(parsed.codexArgs, runtime, manifest.mission_dir);
    return;
  }

  if (parsed.runSubcommand) {
    const repoRoot = resolveRepoRoot(process.cwd());
    const currentPaneId = process.env.TMUX_PANE?.trim();
    if (currentPaneId && launchAutoresearchInSplitPane({
      currentPaneId,
      repoRoot,
      missionDir: parsed.missionDir as string,
      codexArgs: parsed.codexArgs,
    })) {
      return;
    }
  }

  await executeAutoresearchMissionRun(parsed.missionDir as string, parsed.codexArgs);
}