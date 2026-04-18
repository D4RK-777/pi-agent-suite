+ 'Optional: --keep-policy (default: score_improvement)\n\n'
          + `${AUTORESEARCH_HELP}`,
        );
      }
      result = await initAutoresearchMission({
        topic: initOpts.topic,
        evaluatorCommand: initOpts.evaluatorCommand,
        keepPolicy: initOpts.keepPolicy || 'score_improvement',
        slug: initOpts.slug,
        repoRoot,
      });
    } else {
      result = await runGuidedAutoresearchDeepInterview(repoRoot, parsed.seedArgs);
    }

    const currentPaneId = process.env.TMUX_PANE?.trim();
    if (currentPaneId && launchAutoresearchInSplitPane({
      currentPaneId,
      repoRoot,
      missionDir: result.missionDir,
      codexArgs: [],
    })) {
      return;
    }

    await executeAutoresearchMissionRun(result.missionDir, []);
    return;
  }